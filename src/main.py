# smartboard-notebook-exporter
# Copyright (C) 2026  MikeCat2008
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import zip_utils
import svg_editor
import svg_exporter

from pathlib import Path
import tempfile

import mimetypes
import base64

def main(infile, export_type, export_path, export_name, otnextension_bool):
    notebook_path = Path(infile).resolve()  # Get absolute path to the specified file
    if not notebook_path.exists():
        raise FileNotFoundError(f"Path '{notebook_path}' does not exist.")
    if not notebook_path.is_file():
        raise ValueError(f"'{notebook_path}' is not a valid file.")

    notebook_name = notebook_path.stem      # Get name without any extension of the specified file
    notebook_dir = notebook_path.parent

    if export_type not in ['svg-fixed-pages', 'png-pages', 'pdf-svg-pages', 'pdf-png-pages', 'pdf-svg-merged', 'pdf-png-merged']:
        raise ValueError(f"'{export_type}' is not a valid export type.")

    # opt
    if export_path:
        export_path = Path(export_path).resolve()
        if not export_path.exists():
            raise FileNotFoundError(f"Path '{export_path}' does not exist.")
        if not export_path.is_dir():
            raise NotADirectoryError(f"'{export_path}' is not a directory.")
    else:
        export_path = notebook_dir

    # opt
    if not export_name:
        export_name = notebook_name

    if not isinstance(otnextension_bool, bool):
        print(f"'{otnextension_bool}' is not a 'bool'. Adding 'Output Type Name Extension' to output file name.")
        otnextension_bool = True

    tempfile_prefix = f"sbne_{notebook_name}_"
    extracted_dir_name = "extracted"
    fixed_svg_dir_name = "fixed_svg"

    with tempfile.TemporaryDirectory(prefix=tempfile_prefix) as base_tmp_path:
        base_tmp_path = Path(base_tmp_path)
        error_msg = "An error ocurred: "

        try:
            zip_utils.unzip(notebook_path, base_tmp_path, extracted_dir_name)
        except Exception as e:
            raise type(e)(f"{error_msg} {e}")

        extracted_dir = Path(base_tmp_path, extracted_dir_name)
        fixed_svg_dir = Path(base_tmp_path, fixed_svg_dir_name)
        manifest_path = Path(extracted_dir, "imsmanifest.xml")
        if not manifest_path.exists():
            raise FileNotFoundError(f"Path '{manifest_path}' does not exist.")
        if not manifest_path.is_file():
            raise ValueError(f"'{manifest_path}' is not a valid file.")
        try:
            manparser = svg_editor.ManifestParser(manifest_path)
            manparser.load()
            pageorder = manparser.get_pageorder()
        except Exception as e:
            raise type(e)(f"{error_msg} {e}")
        try:
            fixed_svg_dir.mkdir()
        except Exception as e:
            raise type(e)(f"{error_msg} {e}")
        svgs_extracted = extracted_dir.glob("page*.svg")
        for svg in svgs_extracted:
            try:
                editor = svg_editor.SVGManager(svg)
                editor.load()

                svg_cbounds = [float(i) for i in editor.get_svg_attributes("canvas_bounds")]
                # canvas_bounds="{Top X},{Top Y},{Bottom X},{Bottom Y}"
                # "Top" corners from canvas_bounds are allways negative
                svg_width = svg_cbounds[2] - svg_cbounds[0]
                svg_height = svg_cbounds[3] - svg_cbounds[1]

                attrs_dict = {"width":str(svg_width),"height":str(svg_height)}
                editor.update_svg_attributes(attrs_dict)

                # translate(X.xx,Y.yy)
                editor.apply_main_group_transform(f"translate({svg_cbounds[0]*-1},{svg_cbounds[1]*-1})")

                editor.search_image_tag()
                if editor.has_images:
                    XLINK_HREF = "{http://www.w3.org/1999/xlink}href"

                    for img in editor.images:
                        img_width = editor.get_image_attr(img, "width")
                        if img_width:
                            editor.set_image_attr(img, "width", img_width.replace(",","."))

                        img_height = editor.get_image_attr(img, "height")
                        if img_height:
                            editor.set_image_attr(img, "height", img_height.replace(",","."))

                        try:
                            href_path_rel = editor.get_image_attr(img, XLINK_HREF)
                            if not href_path_rel:
                                print(f"Warn: Skipping image '{img}'. Path not found.")
                                continue
                            href_path_abs = extracted_dir / href_path_rel
                            href_mime = mimetypes.guess_type(href_path_abs)[0]
                            with open(href_path_abs, "rb") as href_file:
                                href_b64_string = base64.b64encode(href_file.read()).decode("utf-8")
                            editor.set_image_attr(img, XLINK_HREF, f"data:{href_mime};base64,{href_b64_string}")
                        except Exception as e:
                            print(f"Warn: Skipping image '{img}'. An error ocurred: {e}.")
                            continue

                outfile = fixed_svg_dir / pageorder[svg.name]
                editor.save(outfile)

            except Exception as e:
                raise type(e)(f"{error_msg} {e}")

        try:
            exporter = svg_exporter.SVGExporter(fixed_svg_dir, export_path, export_name, otnextension_bool)
            exporter.export(export_type)
        except Exception as e:
            raise type(e)(f"{error_msg} {e}")

if __name__ == "__main__":
    infile = input("'.notebook' file path: ")
    print("Export types: 'svg-fixed-pages', 'png-pages', 'pdf-svg-pages', 'pdf-png-pages', 'pdf-svg-merged', 'pdf-png-merged'.")
    export_type = input("Export Type: ")
    export_path = input("Export Path (opt): ")
    export_name = input("Export Name (opt): ")
    otnextension_bool = input("Output Name Extension. y/n (y): ")
    if otnextension_bool in ("y","Y","1"):
        otnextension_bool = True
    elif otnextension_bool in ("n","N","0"):
        otnextension_bool = False
    else:
        otnextension_bool = True

    try:
        main(infile, export_type, export_path, export_name, otnextension_bool)
    except Exception as e:
        print(f"An error ocurred: {e}")
