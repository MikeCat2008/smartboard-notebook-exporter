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
import zipfile

def unzip(str_zip_file, str_output_dir_parent, output_dir_name):
    funcion_tag = f"{__name__}.{unzip.__name__}"

    zip_file = Path(str_zip_file).resolve()
    if not zip_file.exists():
        raise FileNotFoundError(f"{funcion_tag}: File '{zip_file}' does not exist.")

    output_dir_parent = Path(str_output_dir_parent).resolve()
    if not output_dir_parent.exists():
        raise FileNotFoundError(f"{funcion_tag}: Parent path '{output_dir_parent}' does not exist.")
    if not output_dir_parent.is_dir():
        raise NotADirectoryError(f"{funcion_tag}: '{output_dir_parent}' is not a directory.")

    output_dir = output_dir_parent / output_dir_name

    if not zipfile.is_zipfile(zip_file):
        raise ValueError(f"{funcion_tag}: '{zip_file}' is not a zip file.")

    try:
        output_dir.mkdir()
        print(f"{funcion_tag}: Directory '{output_dir}' successfully created.")
        print(f"{funcion_tag}: Extracting '{zip_file.name}'...")
        with zipfile.ZipFile(zip_file, "r") as myzip:
            myzip.extractall(path=output_dir)
            print(f"{funcion_tag}: File '{zip_file.name}' successfully extracted in '{output_dir}'.")
            return
    except FileExistsError:
        raise FileExistsError(f"{funcion_tag}: Directory '{output_dir}' already exists.")
    except PermissionError:
        raise PermissionError(f"{funcion_tag}: Permission denied: Unable to create '{output_dir}'.")
    except Exception as e:
        raise type(e)(f"{funcion_tag}: An error occurred: {e}")

def main():
    print(f"\nzip_utils: DEBUGGING: Called 'main()' funcion. Funcion is entended to be used for debugging.")

    print(f"\nzip_utils: DEBUGGING: Testing funcion 'unzip'.")
    z = input("Zip file: ")
    p = input("output_dir_parent: ")
    n = input("output_dir_name: ")
    try:
        unzip(z,p,n)
    except Exception as e:
        print(f"zip_utils: DEBUGGING: An error ocurred with 'unzip': {e}")

    print(f"\nzip_utils: DEBUGGING: No tests remaining. Bye! :3")

if __name__ == "__main__":
    print("zip_utils: 'zip_utils' is running as '__main__'. Program is entended to be used as a module.")
    main()
