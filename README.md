# Smartboard notebook Exporter
<!-- MikeCat made this :3 --->
Export your Smartboard `.notebook` files locally and however you want (and we support).

> **README.md**  
> Read this document in: [ENGLISH](README.md)

---

"Smartboard notebook Exporter" (`sbne`) is a free and open-source project written in Python, designed to export your digital whiteboards from Smartboard `.notebook` files into other types of files (apart from `pdf-png-merged`) while keeping everything local.

This program allows you to take the `.notebook` file (which you can save to external media from your whiteboard) and convert it on your computer. It breaks Smarttech's limitation of only being able to export as a PDF with rasterized bitmaps of each page (`pdf-png-merged`), giving you much more flexibility.

> **DISCLAIMER**  
> This project is not affiliated with Smarttech or any other brand.  
This project is provided "as is", without warranty of any kind.

### How it works
When `sbne` is given a `.notebook` file, it unzips the given file to get access to each page, stored as individual `.svg` files. Then, it fixes each `.svg` to adjust its canvas size and align all the contents to the new canvas. And finally, all the fixed `.svg` files are exported to the desired output type.

### Supported Output Types
- `svg-fixed-pages`: A zip file containing all fixed `.svg` pages.
- `png-pages`: A zip file containing all pages as rasterized `.png` files.
- `pdf-svg-pages`: A zip file containing individual `.pdf` files (vector-based).
- `pdf-svg-merged`: A single PDF file containing all pages as fixed `.svg` (vector-based).
- `pdf-png-pages`: A zip file containing individual `.pdf` files (raster-based).
- `pdf-png-merged`: A single PDF file containing all pages as rasterized `.png` files (raster-based).

### Documentation
- [Format Deep Dive](docs/notebook-format.md): Information about `.notebook` file, its internal structure and how it stores data.
- [Testing Guide](docs/testing.md): Details about test files and how to check that the exporter works properly.

## Requirements
- **Python**: 3.10 or higher.
- **Python Pip**: If not included in Python package, same version as Python.
- **Python venv**: If not included in Python package, same version as Python.
- **Dependencies**: Listed in [`requirements.txt`](requirements.txt).

## Installation

### From Binary
Nothing to see here... (yet!) :3

### From Source
Install and run this program from its source code.

1. Install host dependencies: `python`, `python-pip`, `python-venv` and `git` (optional, download source code manually from this repo).
2. Clone this repo and change the working directory to the new installation dir.
3. Create and activate python virtual environment and name it `.venv`.
4. Install all the required libraries with `pip`	.
5. Run `src/main.py`.

In order to launch again the program after the installation, make sure to be inside the same path where you installed the source code (inside `smartboard-notebook-exporter` folder). Then, activate the same virtual environment (`.venv`) and run `src/main.py`.

<details>
<summary><b>Linux (Debian/Ubuntu)</b></summary>

**Installation and first run:**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv git

git clone https://github.com/MikeCat2008/smartboard-notebook-exporter.git
cd smartboard-notebook-exporter

python3 -m venv .venv
source .venv/bin/activate

pip3 install --no-cache-dir -r requirements.txt

python3 src/main.py
```

**Subsequent runs:**
```bash
source .venv/bin/activate
python3 src/main.py
```

</details>

<!-- The instalation on Windows machines has not been tested -->
<details>
<summary><b>Windows</b></summary>

**Installation and first run:**
```powershell
git clone https://github.com/MikeCat2008/smartboard-notebook-exporter.git
cd smartboard-notebook-exporter

python -m venv .venv
.\.venv\Scripts\activate

pip install -r requirements.txt

python src/main.py
```

**Subsequent runs:**
```powershell	
.\.venv\Scripts\Activate.ps1
python src/main.py
```

</details>

## Usage
After installation, run the program as specified in your installing method.

The CLI will guide you through selecting your `.notebook` file and configuring the parameters for the desired output format.
- **`.notebook` file path**: Path to your `.notebook` file (absolute or relative).
- **Export Type**: Choose one of the 6 output types. 

```bash
~/smartboard-notebook-exporter$ source .venv/bin/activate
(.venv) ~/smartboard-notebook-exporter$ python3 src/main.py
'.notebook' file path: ./tests/01-30-26 11-14-16 AM.notebook
Export types: 'svg-fixed-pages', 'png-pages', 'pdf-svg-pages', 'pdf-png-pages', 'pdf-svg-merged', 'pdf-png-merged'.
Export Type: pdf-svg-merged
zip_utils.unzip: Directory '/tmp/sbne_01-30-26 11-14-16 AM_1uef7kff/extracted' successfully created.
zip_utils.unzip: Extracting '01-30-26 11-14-16 AM.notebook'...
zip_utils.unzip: File '01-30-26 11-14-16 AM.notebook' successfully extracted in '/tmp/sbne_01-30-26 11-14-16 AM_1uef7kff/extracted'.
(.venv) ~/smartboard-notebook-exporter$ ls -l ./tests/01-30-26\ 11-14-16\ AM_pdf-svg-merged.pdf
'./tests/01-30-26 11-14-16 AM_pdf-svg-merged.pdf'
(.venv) ~/smartboard-notebook-exporter$ 
```

## License
This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.