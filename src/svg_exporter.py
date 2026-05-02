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

from pathlib import Path
import re
import io
import zipfile
from cairosvg import svg2pdf, svg2png
import img2pdf
from pypdf import PdfWriter, PdfReader

class SVGExporter:
    def __init__(self, fixed_svg_dir, output_parent_dir, base_name, otnextension_bool):
        funcion_tag = f"{__name__}.{self.__class__.__name__}.{self.__init__.__name__}"

        self.fixed_svg_dir = Path(fixed_svg_dir).resolve()
        # self.fixed_svg_dir is already a PAth object
        if not self.fixed_svg_dir.exists():
            raise FileNotFoundError(f"{funcion_tag}: Fixed SVG directory path '{fixed_svg_dir}' does not exist.")
        if not self.fixed_svg_dir.is_dir():
            raise NotADirectoryError(f"{funcion_tag}: '{fixed_svg_dir}' is not a directory.")

        self.output_parent_dir = Path(output_parent_dir).resolve()
        if not self.output_parent_dir.exists():
            raise FileNotFoundError(f"{funcion_tag}: Parent path '{output_parent_dir}' does not exist.")
        if not self.output_parent_dir.is_dir():
            raise NotADirectoryError(f"{funcion_tag}: '{output_parent_dir}' is not a directory.")

        self.base_name = str(base_name)

        self.otnextension_bool = otnextension_bool
        if not isinstance(self.otnextension_bool, bool):
            raise ValueError(f"'{otnextension_bool}' is not a 'bool'.")

        svg_files_unsorted = list(self.fixed_svg_dir.glob("*.svg"))
        # Try to sort files by lexical order: 0 - 1 - 2 - ... - 9 - 10 - 11 - ...
        self.svg_files = sorted(
            svg_files_unsorted,
            key=lambda p: [int(t) if t.isdigit() else t.lower() for t in re.split(r'(\d+)', p.name)]
        )
        if not list(self.svg_files):
            raise FileNotFoundError(f"{funcion_tag}: Fixed SVG directory '{fixed_svg_dir}' does not contain any SVG ('*.svg') file.")

    def _get_full_path(self, suffix, ext):
        if self.otnextension_bool:
            filename = f"{self.base_name}_{suffix}.{ext}"
        else:
            filename = f"{self.base_name}.{ext}"

        return self.output_parent_dir / filename

    def _export_merged_pdf(self, mode):
        funcion_tag = f"{__name__}.{self.__class__.__name__}.{self._export_merged_pdf.__name__}"
        output_path = self._get_full_path(mode, "pdf")
        merger = PdfWriter()

        for svg in self.svg_files:
            pdf_buffer = io.BytesIO()
            # CairoSVG needs path as a string
            svg_str = str(svg)

            if mode == 'pdf-svg-merged':
                svg2pdf(url=svg_str, write_to=pdf_buffer)
            elif mode == 'pdf-png-merged':
                png_data = svg2png(url=svg_str)
                pdf_buffer = io.BytesIO(img2pdf.convert(png_data))
            else:
                raise ValueError(f"{funcion_tag}: '{mode}' is an invalid mode.")

            pdf_buffer.seek(0)
            merger.append(pdf_buffer)

        with open(output_path, "wb") as f:
            merger.write(f)
        merger.close()

    def _export_zip(self, mode):
        funcion_tag = f"{__name__}.{self.__class__.__name__}.{self._export_zip.__name__}"
        output_path = self._get_full_path(mode, "zip")

        with zipfile.ZipFile(output_path, 'w') as zipf:
            for svg in self.svg_files:
                name_no_ext = svg.stem
                svg_str = str(svg)

                if mode == 'svg-fixed-pages':
                    # SVG -> ZIP
                    zipf.write(svg, arcname=f"{name_no_ext}.svg")

                elif mode == 'png-pages':
                    # SVG -> PNG -> ZIP
                    png_data = svg2png(url=svg_str)
                    zipf.writestr(f"{name_no_ext}.png", png_data)

                elif mode == 'pdf-svg-pages':
                    # SVG -> PDF -> ZIP
                    pdf_data = svg2pdf(url=svg_str)
                    zipf.writestr(f"{name_no_ext}.pdf", pdf_data)

                elif mode == 'pdf-png-pages':
                    # SVG -> PDF -> ZIP
                    png_data = svg2png(url=svg_str)
                    pdf_buffer = io.BytesIO(img2pdf.convert(png_data))
                    zipf.writestr(f"{name_no_ext}.pdf", pdf_buffer.getvalue())

                else:
                    raise ValueError(f"{funcion_tag}: '{mode}' is an invalid mode.")

    def export(self, export_type):
        funcion_tag = f"{__name__}.{self.__class__.__name__}.{self.export.__name__}"

        if export_type in ['svg-fixed-pages', 'png-pages', 'pdf-svg-pages', 'pdf-png-pages']:
            self._export_zip(export_type)
        elif export_type in ['pdf-svg-merged', 'pdf-png-merged']:
            self._export_merged_pdf(export_type)
        else:
            raise ValueError(f"{funcion_tag}: '{export_type}' is an invalid type.")

def main():
    print(f"\nsvg_exporter: DEBUGGING: Called 'main()' function.")

    print(f"\nsvg_exporter: DEBUGGING: Testing class constructor 'SVGExporter'.")
    try:
        fsd = input("Fixed SVG directory path: ")
        opd = input("Output parent directory path: ")
        bn = input("Base '.notebook' file name: ")
        exporter = SVGExporter(fsd, opd, bn)
    except Exception as e:
        print(f"svg_exporter: DEBUGGING: An error ocurred with 'SVGExporter': {e}")
        return

    print(f"\nsvg_exporter: DEBUGGING: Testing class method 'SVGExporter.export()'.")
    try:
        print("Export types: 'svg-fixed-pages', 'png-pages', 'pdf-svg-pages', 'pdf-png-pages', 'pdf-svg-merged', 'pdf-png-merged'.")
        et = input("Export Type: ")
        exporter.export(et)
    except Exception as e:
       print(f"svg_exporter: DEBUGGING: An error ocurred with 'SVGExporter.export()': {e}")
       return

    print(f"\nsvg_exporter: DEBUGGING: No tests remaining. Bye! :3")

if __name__ == "__main__":
    print("svg_exporter: DEBUGGING: Running as '__main__'.")
    main()
