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

### Binary
- [***Tha binary***](https://github.com/MikeCat2008/smartboard-notebook-exporter/releases/latest) :3  
No requirements at all, only download the executable compatible with your computer and that's all! :D

### Source code
- **Python**: 3.10 or higher (3.12 or 3.13 recomended).
- **Python Pip**: If not included in Python package, same version as Python.
- **Python venv**: If not included in Python package, same version as Python.
- **Python Tkinter**: If not included in Python package, same version as Python.
- **System Dependencies**: Cairo.
- **Dependencies**: Listed in [`requirements.txt`](requirements.txt).

## Installation

### From Binary
Download and run this program from a fully portable binary. No administrator/superuser permission required. Only GUI (Graphics User Interface) available.

You only need to download the binary specific for your OS (Windows, Linux...) and Host Architecture (AMD64, ARM64...) from this repository [Releases Tab](https://github.com/MikeCat2008/smartboard-notebook-exporter/releases/latest) and execute this program. If your OS/Host Architecture does not appear on the Releases Tab, you will need to install this program from source and run it or build a binary specific for your device.

**Available Binaries**

<table>
    <thead>
        <tr>
            <th>Operating System</th>
            <th>Version</th>
            <th>Architecture</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Debian</td>
            <td>Debian 13 Trixie</td>
            <td>AMD64</td>
        </tr>
        <tr>
            <td rowspan="2">Windows</td>
            <td>Windows 10</td>
            <td>AMD64</td>
        </tr>
        <tr>
            <td>Windows 11</td>
            <td>AMD64</td>
        </tr>
    </tbody>
</table>

> **DISCLAIMER**  
> The only trusted source of compiled binaries of this program is this [GitHub Repository](https://github.com/MikeCat2008/smartboard-notebook-exporter).  
> Other download mirrors or sources can be a potential risk of viruses or other kind of malware. This is because binaries are just the machine code (a bunch of ones and zeros) created from a source code, which can hardly be traced back to that origin. Therefore, two binaries could look identical but behave in very different ways. Checking the SHA256 of the binaries is highly encouraged.

### From Source
Install and run this program from its source code.

<details>
<summary><b>Linux (Debian/Ubuntu)</b></summary>

**Installation and first run**

1. **System dependencies installation**: `python`, `pip`, `venv`, `tkinter`, `git` and CairoSVG libraries (`libcairo2`, `libffi-dev` and `python3-dev`) . Access to `sudo` is required (unless dependencies are already fulfilled, in that case go to the next step).

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv python3-tk git libcairo2 libffi-dev python3-dev
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

4. **Run**: Run either the Command Line Interface (CLI) with `src/main.py` or the Graphical User Interface (GUI) with `src/gui.py`.

```bash
python3 src/main.py # CLI
python3 src/gui.py  # GUI
```

**Subsequent runs:**

In order to launch again the program after the installation, make sure to be inside the same folder where you cloned the source code. Then, activate the same virtual environment (`.venv`) and run the desired User Interface.

```bash
source .venv/bin/activate
python3 src/main.py # CLI
python3 src/gui.py  # GUI
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

4. **Run**: Run either the Command Line Interface (CLI) with `src/main.py` or the Graphical User Interface (GUI) with `src/gui.py`.

```powershell
python src\main.py # CLI
python src\gui.py  # GUI
```

**Subsequent runs:**

In order to launch again the program after the installation, make sure to be inside the same folder where you cloned the source code. Then, activate the same virtual environment (`.venv`) and run the desired User Interface.

```powershell	
.venv\Scripts\activate
python src\main.py # CLI
python src\gui.py  # GUI
```

</details>

## Building
In order to build a binary of this program, it is required to have previously done the installaton from source and at least one run to ensure that everything is working correctly with the installation.

To build this program, activate the virtual environment (`.venv`) of the installation and run the `build` script that corresponds to the OS where the installation has been done: `.sh` for Linux based and `.bat` for Windows. When the script finishes packing and building the program, the resulting binary will be placed in the folder `dist/` inside the main directory of this project. This binary is fully portable and does not require superuser/administrator permission to run.

The building script uses PyInstaller to pack the source code among the python interpreter, all python libraries required and any system libraries which are required by the python libraries, inside one single and portable executable. It is important to mention that the binaries produced by PyInstaller are not cross-compatible, meaning that, for example, a binary compiled for Windows, won't run on Debian or viceversa.

## Usage
In order to export your `.notebook` file into the desired output format it is needed to configure the following parameters:
- **`.notebook` file path**: Path to your `.notebook` file (absolute or relative to the path where the program has been launched).
- **Export Type**: Choose one of the 6 output types. 
- **Export Path** (optional): Change the output directory for your output file. If left blank, the output directory will be the same where the `.notebook` has been taken from.
- **Export Name** (optional): Change the output file name. If left blank, the output name will be the same as the input `.notebook` file.
- **Output Name Extension**: Boolean flag to append to the export name "_`Output Type`". If left blank or invalid input, it will be assumed as the default (y, yes).

Any exported file will end with its respective ".`Output Type Extension`".

After installation, run the program as specified in your installing method.

### GUI
Graphical User Interface. The GUI is available in both binary releases and source code installations. It is the recommended option for most users.

**Usage**

When the program's GUI opens, the user will be prompted from top to bottom with the application name, the version management section, the GUI language selection, all the fields to configure all the parameters needed to export the notebook file, the export button and useful links.

At the version management section the user can see the current build version of the app and check for updates. The `Check Updates` button is a link to the [Latest Release](https://github.com/MikeCat2008/smartboard-notebook-exporter/releases/latest) GitHub page, where the user can download the newest build of the app. It is highly recommended to check from time to time this page in order to be up to date with feature updates and bug fixes.

The language selection section shows the user the current language that is being used for the GUI and the buttons to choose the available languages. English is the default language.

The first group of fields is `Notebook File`, which lets the user choose what `.notebook` file to export by specifying the path to that file. The file can be specified by either typing the relative path to where the app has been launched or the absolute path, or selecting the file by pressing the `BROWSE` button. Only `.notebook` files are allowed. If the path to the file is empty, doesn't exist or is not a valid file, when trying to export, a window with an error will appear.

The second group of fields is `Export File`, which lets the user configure the output file. The `Output Folder` field behaves like the Notebook File field but it only allows valid relative or absolute paths to folders instead of files. If left blank, the file will be output to the same directory as the file that is being exported. The `Name` field lets the user choose a custom name for the output file. If left blank, the file will use the same name as the file that is being exported. The `Output Type` selection field lets the user choose among the available export types. The `Extension Name Toggle` toggle adds an identifier for the output type chosen for the output file. Below there is a live preview of the name of the output file, including the custom (or default) name, the extension name (if activated) and the output extension that corresponds with the output type selected.

When the export button is pressed, it will start the export process while also giving feedback to the user by disabling itself and changing its appearance. This process will usualy end by outputing the output file and showing an info pop-up window. The export process might be interrupted if there are invalid parameters, file overwrite risk or in the event that an error occurs while exporting, which will result in an interruption of this shown by a warning/error pop-up window. After the export process is over (wether it has been successful or not), the export button will re-enable itself.

The useful links will open the users default browser when clicked. These links are this [GitHub Repository](https://github.com/MikeCat2008/smartboard-notebook-exporter) and the [GPLv3 License](https://www.gnu.org/licenses/gpl-3.0.html).

### CLI
Command Line Interface. Only available throught source code execution.

**Usage**
```text
(.venv) $ python src/main.py
'.notebook' file path: ./tests/01-30-26 11-14-16 AM.notebook
Export types: 'svg-fixed-pages', 'png-pages', 'pdf-svg-pages', 'pdf-png-pages', 'pdf-svg-merged', 'pdf-png-merged'.
Export Type: pdf-svg-merged
Export Path (opt): ./
Export Name (opt): 
Output Name Extension. y/n (y): Y

(.venv) $ 
```

```text
[dir] . # Current Directory
├─[dir] tests
| └─ [notebook] 01-30-26 11-14-16 AM.notebook
└─ [pdf] 01-30-26 11-14-16 AM_pdf-svg-merged.pdf
```

## License
This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.
