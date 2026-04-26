import zip_utils
import svg_editor
import svg_exporter

from pathlib import Path
import tempfile

def main(infile, export_type):
    notebook_path = Path(infile).resolve()  # Get absolute path to the specified file
    if not notebook_path.exists():
        print(f"Path '{notebook_path}' does not exist.")
        return
    if not notebook_path.is_file():
        print(f"'{notebook_path}' is not a file.")
        return

    notebook_name = notebook_path.stem      # Get name without any extension of the specified file
    notebook_dir = notebook_path.parent

    if export_type not in ['svg-fixed-pages', 'png-pages', 'pdf-svg-pages', 'pdf-png-pages', 'pdf-svg-merged', 'pdf-png-merged']:
        print(f"'{export_type}' is not a valid export type.")
        return

    tempfile_prefix = f"sbne_{notebook_name}_"
    extracted_dir_name = "extracted"
    fixed_svg_dir_name = "fixed_svg"

    with tempfile.TemporaryDirectory(prefix=tempfile_prefix) as base_tmp_path:
        base_tmp_path = Path(base_tmp_path)
        error_msg = "An error ocurred: "

        try:
            zip_utils.unzip(notebook_path, base_tmp_path, extracted_dir_name)
        except Exception as e:
            print(error_msg)

        extracted_dir = base_tmp_path / extracted_dir_name
        fixed_svg_dir = base_tmp_path / fixed_svg_dir_name
        try:
            fixed_svg_dir.mkdir()
        except Exception as e:
            print(f"{error_msg} {e}")
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

                outfile = fixed_svg_dir / svg.name
                editor.save(outfile)

            except Exception as e:
                print(f"{error_msg} {e}")
                return

        try:
            exporter = svg_exporter.SVGExporter(fixed_svg_dir, notebook_dir, notebook_name)
            exporter.export(export_type)
        except Exception as e:
            print(f"{error_msg} {e}")
            return

if __name__ == "__main__":
    infile = input("'.notebook' file path: ")
    print("Export types: 'svg-fixed-pages', 'png-pages', 'pdf-svg-pages', 'pdf-png-pages', 'pdf-svg-merged', 'pdf-png-merged'.")
    export_type = input("Export Type: ")
    main(infile, export_type)
