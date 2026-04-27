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
- **Python**: 3.10 or higher (3.12 or 3.13 recomended).
- **Python Pip**: If not included in Python package, same version as Python.
- **Python venv**: If not included in Python package, same version as Python.
- **System Dependencies**: Cairo.
- **Dependencies**: Listed in [`requirements.txt`](requirements.txt).

## Installation

### From Binary
Nothing to see here... (yet!) :3

### From Source
Install and run this program from its source code.

<details>
<summary><b>Linux (Debian/Ubuntu)</b></summary>

**Installation and first run**

1. **System dependencies installation**: `python`, `pip`, `venv`, `git` and CairoSVG libraries (`libcairo2`, `libffi-dev` and `python3-dev`) . Access to `sudo` is required (unless dependencies are already fulfilled, in that case go to the next step).

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv git libcairo2 libffi-dev python3-dev
```

2. **Clone source code**: Clone this repo and change the working directory to the new installation dir.

```bash
git clone https://github.com/MikeCat2008/smartboard-notebook-exporter.git
cd smartboard-notebook-exporter
```

3. **Python enviroment setup**: Create and activate python virtual environment and name it `.venv`. Install all the required libraries listed in `requirements.txt` with `pip`.

```bash
python3 -m venv .venv
source .venv/bin/activate

pip3 install -r requirements.txt
```

4. **Run**:

```bash
python3 src/main.py
```

**Subsequent runs:**

In order to launch again the program after the installation, make sure to be inside the same folder where you cloned the source code. Then, activate the same virtual environment (`.venv`) and run `src/main.py`.

```bash
source .venv/bin/activate
python3 src/main.py
```

</details>

<details>
<summary><b>Windows</b></summary>

**Installation and first run:**

1. **System dependencies installation**: `python`, `git` and [GTK Runtime](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer) (for CairoSVG). Access to Administrator mode is required (unless dependencies are already fulfilled, in that case go to the next step).

```powershell
# Run this in a terminal as Administrator
winget install python Git.Git tschoonj.GTKForWindows
exit
```

> **NOTE**  
> After installing all system dependencies, closing the terminal with `exit` and opening a new one is required for the system PATH to update.

2. **Clone source code**: Clone this repo and change the working directory to the new installation dir.

```powershell
git clone https://github.com/MikeCat2008/smartboard-notebook-exporter.git
cd smartboard-notebook-exporter
```

3. **Python enviroment setup**: Create and activate python virtual environment and name it `.venv`. Install all the required libraries listed in `requirements.txt` with `pip`.

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

4. **Run**:

```powershell
python src/main.py
```

**Subsequent runs:**

In order to launch again the program after the installation, make sure to be inside the same folder where you cloned the source code.

```powershell	
.venv\Scripts\activate
python src\main.py
```

</details>

## Usage
After installation, run the program as specified in your installing method.

The CLI will guide you through selecting your `.notebook` file and configuring the parameters for the desired output format.
- **`.notebook` file path**: Path to your `.notebook` file (absolute or relative).
- **Export Type**: Choose one of the 6 output types. 

```text
(.venv) $ python src/main.py
'.notebook' file path: ./tests/01-30-26 11-14-16 AM.notebook
Export types: 'svg-fixed-pages', 'png-pages', 'pdf-svg-pages', 'pdf-png-pages', 'pdf-svg-merged', 'pdf-png-merged'.
Export Type: pdf-svg-merged
(.venv) $ 
```

The exported file will be stored in the same path as the chosen `.notebook` file. The naming scheme of this output file is: `Original File Name`_`Output Type`.`Output Type Extension`

```text
[dir] tests
├─ [notebook] 01-30-26 11-14-16 AM.notebook
└─ [pdf] 01-30-26 11-14-16 AM_pdf-svg-merged.pdf
```

## License
This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.