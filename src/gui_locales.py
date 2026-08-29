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

locales = {
    "es": {
        "lbl_help": "Ayuda",
        "lbl_ver": "Versión",
        "lbl_ver_curtxt": "Actual:",
        "btn_ver_chkupd": "Comprobar Actualizaciones",
        "lbl_lang": "Idioma",
        "lbl_lang_info": "Español (Spanish)",
        "lbl_nbfile": "Archivo Notebook",
        "btn_nbfile_browse": "BUSCAR",
        "lbl_expfile": "Exportar Archivo",
        "lbl_expfile_outdir": "Carpeta de Salida (Opcional)",
        "btn_expfile_outdir": "BUSCAR",
        "lbl_expfile_name": "Nombre (Opcional)",
        "lbl_expfile_outtype": "Formatos de Salida",
        "chkbtn_expfile_outtypeext": "Añadir Etiqueta de Conversión",
        "lbl_expfile_nameprev": "Previsualización del Nombre:",
        "btn_export": "EXPORTAR",
        "btn_export_active": "EXPORTANDO...",
        "msgbox_warn_missfile_msg": "Archivo Faltante",
        "msgbox_warn_missfile_dtl": "Porfavor, selecciona un archivo .notebook antes.",
        "msgbox_warn_fileow_msg": "Aviso de Sobreescritura de Archivos",
        "msgbox_warn_fileow_dtl": f"Ya existe un archivo con ese nombre. ¿Sobreescribir archivo?\nEsta acción no puede ser deshecha.",
        "msgbox_info_ok_msg": "Éxito!",
        "msgbox_info_ok_dtl": "Su archivo ha sido exportado existosamente.",
        "msgbox_err_exp_msg": "Error durante la Exportación",
        "msgbox_err_exp_dtl": "Algo fue mal:",
        "link_repo": "Repositorio de GitHub",
        "link_license": "Licencia GPLv3",

        "btn_help1_tuto": "Tutorial",
        "btn_help2_outtypes": "Formatos de Salida",
        "btn_help_exit": "SALIR",
        "lbl_help1_pages": [
            "Bienvenido a SBNE. ¡Exporta tus archivos Smartboard '.notebook' como quieras! :D",
            "Consigue tu pizarra digital desde tu Smartboard compartiendola a un almacenamiento externo.",
            "Elige tu '.notebook' escribiendo la ruta al archivo o buscándolo con el botón.",
            "Configura como quieres exportar tu pizarra digital.",
            "Elige una carpeta de salida. (Opcional, vacío es la misma carpeta de donde has tomado el '.notebook')",
            "Da a tu archivo de salida un nombre distinto al del original. (Opcional)",
            "Elige el formato de salida al que quieres exportar. Más información en Ayuda>Formatos de Salida",
            "Añade la extensión de tipo de conversión al final del nombre del archivo.",
            "Mira cómo el nombre del archivo de salida será.",
            "Una vez todo esté configurado, ¡Exporta tu archivo pulsando el botón!",
            "Para más información, haz click en 'Repositorio de GitHub' :3"
        ],
        "lbl_help2_pages": [
            "'svg-fixed-pages': Archivo zip con las páginas '.svg'.",
            "'png-pages': Archivo zip con las páginas rasterizadas en '.png'.",
            "'pdf-svg-pages': Archivo zip con las páginas como archivos '.pdf' individuales (contenido vectorial).",
            "'pdf-svg-merged': Único archivo PDF con las páginas como archivos '.svg' (contenido vectorial).",
            "'pdf-png-pages': Archivo zip con las páginas como archivos '.pdf' individuales (contenido rasterizado).",
            "'pdf-png-merged': Único archivo PDF con las páginas rasterizadas en '.png' (contenido rasterizado)."
        ],

        "test": "Me gustan los furros :3" # nadie lo sabrá >w< - MikeCat2008
    },
    "en": {
        "lbl_help": "Help",
        "lbl_ver": "Version",
        "lbl_ver_curtxt": "Current:",
        "btn_ver_chkupd": "Check Updates",
        "lbl_lang": "Language",
        "lbl_lang_info": "English (English)",
        "lbl_nbfile": "Notebook File",
        "btn_nbfile_browse": "BROWSE",
        "lbl_expfile": "Export File",
        "lbl_expfile_outdir": "Output Folder (Optional)",
        "btn_expfile_outdir": "BROWSE",
        "lbl_expfile_name": "Name (Optional)",
        "lbl_expfile_outtype": "Output Type",
        "chkbtn_expfile_outtypeext": "Extension Name Toggle",
        "lbl_expfile_nameprev": "Name Preview:",
        "btn_export": "EXPORT",
        "btn_export_active": "EXPORTING...",
        "msgbox_warn_missfile_msg": "Missing File",
        "msgbox_warn_missfile_dtl": "Please, select a .notebook file first.",
        "msgbox_warn_fileow_msg": "File Overwrite Warning",
        "msgbox_warn_fileow_dtl": f"A file with that name already exists. Overwrite file?\nThis action cannot be reversed.",
        "msgbox_info_ok_msg": "Success!",
        "msgbox_info_ok_dtl": "Your file has been successfuly exported",
        "msgbox_err_exp_msg": "Error while Exporting",
        "msgbox_err_exp_dtl": "Something went wrong:",
        "link_repo": "GitHub Repository",
        "link_license": "GPLv3 License",

        "btn_help1_tuto": "Tutorial",
        "btn_help2_outtypes": "Output Types",
        "btn_help_exit": "EXIT",
        "lbl_help1_pages": [
            "Welcome to SBNE. Export your Smartboard '.notebook' however you want! :D",
            "Get your digital whiteboard from your Smartboard by sharing it to an external storage.",
            "Select your '.notebook' file by typing the file path or by browsing with the button.",
            "Configure how you want to export your digital whiteboard.",
            "Choose an output folder. (Optional, if left blank output folder is the same where you took the '.notebook')",
            "Give your output file a different name from the original. (Optional)",
            "Choose the output type that you want to export to. More info in Help>Output Types",
            "Add an output name extension at the end of the filename showing the output type choosen.",
            "Look how the output filename will be.",
            "Once everything is configured, export your file by pressing the button!",
            "For more info, click on 'GitHub Repository' :3"
        ],
        "lbl_help2_pages": [
            "svg-fixed-pages: zip file containing all fixed .svg pages.",
            "png-pages: zip file containing all pages as rasterized .png files.",
            "pdf-svg-pages: zip file containing individual .pdf files (vector-based).",
            "pdf-svg-merged: Single PDF file containing all pages as fixed .svg (vector-based).",
            "pdf-png-pages: zip file containing individual .pdf files (raster-based).",
            "pdf-png-merged: single PDF file containing all pages as rasterized .png files (raster-based)."
        ],

        "test": "I like furries :3" # nobody's gonna know >w< - MikeCat2008
    }
}
