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

# 'No nos importa perdedor 🗣️🗣️🔥🔥'

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
            "Para más información, haz click en 'tetas' o cualquier anuncio :3"
        ],
        "lbl_help2_pages": [
            "'hola': Archivo zip con las páginas '.svg'. (HAIIIIIIII!!!!!)",
            "'endogamia': Archivo zip con las páginas rasterizadas en '.png'. (José Pérez Pérez Pérez Pérez Pérez ...)",
            "'parafilia': Archivo zip con las páginas como archivos '.pdf' individuales (contenido vectorial). (Fetichista vs Masoca)",
            "'tungsteno': Único archivo PDF con las páginas como archivos '.svg' (contenido vectorial). (W W W sahur)",
            "'cloroformo': Archivo zip con las páginas como archivos '.pdf' individuales (contenido rasterizado). (El desayuno de los campeones)",
            "'estrogeno': Único archivo PDF con las páginas rasterizadas en '.png' (contenido rasterizado). (Ojala)"
        ],

        "export_types": {
            'hola': 'svg-fixed-pages',
            'endogamia': 'png-pages',
            'parafilia': 'pdf-svg-pages',
            'tungsteno': 'pdf-svg-merged',
            'cloroformo': 'pdf-png-pages',
            'estrogeno': 'pdf-png-merged'
        },
        
        "anuncio_1": "tetas",
        "test": "Me gustan los furros :3" # todos lo sabrán >w< - MikeCat2008
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
            "For more info, click on 'tits' or any ad :3"
        ],
        "lbl_help2_pages": [
            "svg-fixed-pages: zip file containing all fixed .svg pages.",
            "png-pages: zip file containing all pages as rasterized .png files.",
            "pdf-svg-pages: zip file containing individual .pdf files (vector-based).",
            "pdf-svg-merged: Single PDF file containing all pages as fixed .svg (vector-based).",
            "pdf-png-pages: zip file containing individual .pdf files (raster-based).",
            "pdf-png-merged: single PDF file containing all pages as rasterized .png files (raster-based)."
        ],

        "export_types": {
            'svg-fixed-pages': 'svg-fixed-pages',
            'png-pages': 'png-pages',
            'pdf-svg-pages': 'pdf-svg-pages',
            'pdf-svg-merged': 'pdf-svg-merged',
            'pdf-png-pages': 'pdf-png-pages',
            'pdf-png-merged': 'pdf-png-merged'
        },

        "anuncio_1": "tits",
        "test": "I like furries :3" # everybody's gonna know >w< - MikeCat2008
    },

    "uwu": {
            "lbl_help": "uwu",
            "lbl_ver": "uwu",
            "lbl_ver_curtxt": "uwu:",
            "btn_ver_chkupd": "uwu uwu",
            "lbl_lang": "uwu",
            "lbl_lang_info": "uwu (uwu)",
            "lbl_nbfile": "uwu uwu",
            "btn_nbfile_browse": "uwu",
            "lbl_expfile": "uwu uwu",
            "lbl_expfile_outdir": "uwu uwu (uwun't)",
            "btn_expfile_outdir": "uwu",
            "lbl_expfile_name": "uwu (uwun't)",
            "lbl_expfile_outtype": "uwu uwu",
            "chkbtn_expfile_outtypeext": "uwu uwu uwu",
            "lbl_expfile_nameprev": "uwu uwu:",
            "btn_export": "uwu",
            "btn_export_active": "owo",
            "msgbox_warn_missfile_msg": "unu unu",
            "msgbox_warn_missfile_dtl": "uwu, uwu uwu .uwu uwu uwu.",
            "msgbox_warn_fileow_msg": "unu unu unu",
            "msgbox_warn_fileow_dtl": f"uwu uwu uwu uwu uwu uwu uwu. uwu uwu?\nuwu uwu uwu uwu uwu.",
            "msgbox_info_ok_msg": ">w<!",
            "msgbox_info_ok_dtl": "uwu uwu uwu uwu uwu uwu",
            "msgbox_err_exp_msg": "unu unu unu",
            "msgbox_err_exp_dtl": "uwu uwu uwu:",
            "link_repo": "uwu uwu",
            "link_license": "uwu uwu",
    
            "btn_help1_tuto": "uwu",
            "btn_help2_outtypes": "uwu uwu",
            "btn_help_exit": "uwu",
            "lbl_help1_pages": [
                "uwu",
                "uwu",
                "uwu",
                "uwo",
                "owo",
                "owo",
                "-w-",
                "owo",
                "-w-",
                "owo",
                "TETAS GORDASSSSS ASDASDJHASDHBASIKFHUASIDHISOAHDIOSAHDIUASHDIUHIFUG"
            ],
            "lbl_help2_pages": [
                "uwu1: a",
                "uwu2: nadie",
                "uwu3: le",
                "uwu4: importa",
                "uwu5: perdedor",
                "uwu6: 🗣️🗣️🔥🔥"
            ],
    
            "export_types": {
                'uwu1': 'svg-fixed-pages',
                'uwu2': 'png-pages',
                'uwu3': 'pdf-svg-pages',
                'uwu4': 'pdf-svg-merged',
                'uwu5': 'pdf-png-pages',
                'uwu6': 'pdf-png-merged'
            },
    
            "anuncio_1": "OWO",
            "test": "Bombarden Yucatec" # porfa - MikeCat2008, seguro, yo le concozco. Es furro dice
        }
}

# Mamar pene deberia ser deporte olímpico

# Maming dih should be olimpic sport

# uwu
