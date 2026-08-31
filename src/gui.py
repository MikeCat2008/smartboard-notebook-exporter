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

from textwrap import wrap

import gui_locales
import main

import tkinter as tk
from tkinter import ttk, filedialog

import webbrowser

from PIL import Image, ImageTk

from pathlib import Path

import os
SRC_PATH = os.path.dirname(os.path.abspath(__file__)) +'/'

class ExporterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smartboard Notebook Exporter")
        self.root.configure(bg="#f5f5f5")

        # --- VARIABLES ---
        ## --- i18n ---
        self.var_lang = "en" # Set default language: "en","es"
        ## --- main ---
        self.var_nbfile = tk.StringVar(value="")
        self.var_expfile_outdir = tk.StringVar(value="")
        self.var_expfile_name = tk.StringVar(value="")
        self.var_expfile_outtype = tk.StringVar()
        self.var_expfile_outtypeext = tk.BooleanVar(value=True)
        ## --- Name Preview ---
        ## Update variables whenever there's something new to update name preview
        self.var_expfile_nameprev = None
        self.var_nbfile.trace_add("write", self.expfile_nameprev_update)
        self.var_expfile_name.trace_add("write", self.expfile_nameprev_update)
        self.var_expfile_outtype.trace_add("write", self.expfile_nameprev_update)
        self.var_expfile_outtypeext.trace_add("write", self.expfile_nameprev_update)
        ## --- Export Status ---
        self.var_export_active = tk.BooleanVar(value=False)
        ## --- Help ---
        self.var_help1_active = False
        self.var_help1_pindex = 1
        self.var_help1_page_min = 1
        self.var_help1_page_max = 11
        self.var_help2_active = False
        self.var_help2_pindex = 4
        self.var_help2_page_min = 1
        self.var_help2_page_max = 6

        # --- VISUAL ELEMENTS LAYOUT ---
        self.main_frame = tk.Frame(root, bg="#f5f5f5", padx=20, pady=20)
        self.main_frame.pack()

        ## --- App Name ---
        tk.Label(self.main_frame, text="Smartboard notebook Exporter", font=("Arial", 20, "bold"), bg="#f5f5f5", fg="#333").grid(row=0, column=0, columnspan=4, pady=(0, 10))

        ttk.Separator(self.main_frame, orient='horizontal').grid(row=1, column=0, columnspan=4, sticky="ew", pady=(0, 10))

        ## --- Config and Help Tabs ---
        self.ntbk_confhelp = ttk.Notebook(self.main_frame)
        self.ntbk_confhelp.grid(row=2, column=0, columnspan=4, sticky="ew")

        ### --- i18n Tab ---
        self.confhelp_tab1_i18n = tk.Frame(self.ntbk_confhelp, bg="#f5f5f5", padx=5, pady=5)
        self.ntbk_confhelp.add(self.confhelp_tab1_i18n)

        self.lbl_lang = tk.Label(self.confhelp_tab1_i18n, font=("Arial", 12, "bold"), bg="#f5f5f5")
        self.lbl_lang.grid(row=0, column=0, sticky="w", pady=(0,5))

        self.lbl_lang_info = tk.Label(self.confhelp_tab1_i18n, font=("Arial", 10), bg="#f5f5f5")
        self.lbl_lang_info.grid(row=1, column=0, sticky="w")

        self.frame_lang = tk.Frame(self.confhelp_tab1_i18n, bg="#f5f5f5")
        self.frame_lang.grid(row=2, column=0, columnspan=2, sticky="w")

        self.btn_lang_es = tk.Button(self.frame_lang, text="ES", width="3", command=lambda: self.set_lang("es"))
        self.btn_lang_es.grid(row=0, column=0, sticky="w", padx=(0, 5))

        self.btn_lang_en = tk.Button(self.frame_lang, text="EN", width="3", command=lambda: self.set_lang("en"))
        self.btn_lang_en.grid(row=0, column=1, sticky="w", padx=(0, 5))

        self.btn_lang_en = tk.Button(self.frame_lang, text="UWU", width="3", command=lambda: self.set_lang("uwu"))
        self.btn_lang_en.grid(row=0, column=2, sticky="w", padx=(0, 5))

        ### --- Version Tab ---
        self.confhelp_tab2_ver = tk.Frame(self.ntbk_confhelp, bg="#f5f5f5", padx=5, pady=5)
        self.ntbk_confhelp.add(self.confhelp_tab2_ver)

        self.lbl_ver = tk.Label(self.confhelp_tab2_ver, font=("Arial", 12, "bold"), bg="#f5f5f5")
        self.lbl_ver.grid(row=0, column=0, sticky="w", pady=(0,5))

        self.lbl_ver_curtxt = tk.Label(self.confhelp_tab2_ver, font=("Arial", 10), bg="#f5f5f5")
        self.lbl_ver_curtxt.grid(row=1, column=0, sticky="w")

        self.lbl_ver_cur = tk.Label(self.confhelp_tab2_ver, text="v1.3.0", font=("Arial", 10, "bold"), bg="#f5f5f5")
        self.lbl_ver_cur.grid(row=1, column=1, sticky="e")

        self.btn_ver_chkupd = tk.Button(self.confhelp_tab2_ver, command=lambda: webbrowser.open_new("https://github.com/MikeCat2008/smartboard-notebook-exporter/releases/latest"))
        self.btn_ver_chkupd.grid(row=2, column=0, columnspan=2, sticky="ew", padx=(0,10))

        ### --- Help Tab ---
        self.confhelp_tab3_help = tk.Frame(self.ntbk_confhelp, bg="#f5f5f5", padx=5, pady=5)
        self.ntbk_confhelp.add(self.confhelp_tab3_help)

        self.lbl_help = tk.Label(self.confhelp_tab3_help, font=("Arial", 12, "bold"), bg="#f5f5f5")
        self.lbl_help.grid(row=0, column=0, sticky="w", pady=(0,10))

        self.btn_help1_tuto = tk.Button(self.confhelp_tab3_help, text="Tutorial", command=self.help1_tuto)
        self.btn_help1_tuto.grid(row=1, column=0, sticky="w", padx=(0,10))

        self.lbl_help1_page = tk.Label(self.confhelp_tab3_help, font=("Arial", 10), bg="#f5f5f5")
        self.frame_help1_pcntl = tk.Frame(self.confhelp_tab3_help, bg="#f5f5f5")
        self.lbl_help1_pindex = tk.Label(self.frame_help1_pcntl, font=("Arial", 10), bg="#f5f5f5")
        self.btn_help1_prev = tk.Button(self.frame_help1_pcntl, text="<", width="1", command=lambda: self.help1_tuto_pages(False), state="disabled")
        self.btn_help1_next = tk.Button(self.frame_help1_pcntl, text=">", width="1", command=lambda: self.help1_tuto_pages(True), state="disabled")
        self.btn_help1_exit = tk.Button(self.frame_help1_pcntl, command=self.help1_tuto_exit)

        self.btn_help2_outtypes = tk.Button(self.confhelp_tab3_help, text="Output Types", command=self.help2_outtypes)
        self.btn_help2_outtypes.grid(row=1, column=1, sticky="w")

        self.lbl_help2_page = tk.Label(self.confhelp_tab3_help, font=("Arial", 10), bg="#f5f5f5")
        self.frame_help2_pcntl = tk.Frame(self.confhelp_tab3_help, bg="#f5f5f5")
        self.lbl_help2_pindex = tk.Label(self.frame_help2_pcntl, font=("Arial", 10), bg="#f5f5f5")
        self.btn_help2_prev = tk.Button(self.frame_help2_pcntl, text="<", width="1", command=lambda: self.help2_outtypes_pages(False), state="disabled")
        self.btn_help2_next = tk.Button(self.frame_help2_pcntl, text=">", width="1", command=lambda: self.help2_outtypes_pages(True), state="disabled")
        self.btn_help2_exit = tk.Button(self.frame_help2_pcntl, command=self.help2_outtypes_exit)

        ttk.Separator(self.main_frame, orient='horizontal').grid(row=3, column=0, columnspan=4, sticky="ew", pady=(10, 10))

        ## --- Notebook File Section ---
        self.lbl_nbfile = tk.Label(self.main_frame, font=("Arial", 14, "bold"), bg="#f5f5f5")
        self.lbl_nbfile.grid(row=5, column=0, sticky="w")

        self.ent_nbfile = tk.Entry(self.main_frame, textvariable=self.var_nbfile, width=40)
        self.ent_nbfile.grid(row=6, column=0, columnspan=3, sticky="ew", padx=(0, 10), pady=10)

        self.btn_nbfile_browse = tk.Button(self.main_frame, command=self.nbfile_search)
        self.btn_nbfile_browse.grid(row=6, column=3, sticky="ew")

        ## --- Export File Section ---
        self.lbl_expfile = tk.Label(self.main_frame, font=("Arial", 14, "bold"), bg="#f5f5f5")
        self.lbl_expfile.grid(row=7, column=0, sticky="w", pady=(20, 5))

        ### Output Directory
        self.lbl_expfile_outdir = tk.Label(self.main_frame, font=("Arial", 10), bg="#f5f5f5")
        self.lbl_expfile_outdir.grid(row=8, column=0, sticky="w")

        self.ent_expfile_outdir = tk.Entry(self.main_frame, textvariable=self.var_expfile_outdir)
        self.ent_expfile_outdir.grid(row=9, column=0, columnspan=3, sticky="ew", padx=(0, 10), pady=5)

        self.btn_expfile_outdir = tk.Button(self.main_frame, command=self.expfile_outfold_search)
        self.btn_expfile_outdir.grid(row=9, column=3, sticky="ew")

        ### Custom Name
        self.lbl_expfile_name = tk.Label(self.main_frame, font=("Arial", 10), bg="#f5f5f5")
        self.lbl_expfile_name.grid(row=10, column=0, sticky="w", pady=(10, 0))

        self.ent_expfile_name = tk.Entry(self.main_frame, textvariable=self.var_expfile_name)
        self.ent_expfile_name.grid(row=11, column=0, sticky="ew", padx=(0, 5))

        ### Output Type
        self.lbl_expfile_outtype = tk.Label(self.main_frame, font=("Arial", 10), bg="#f5f5f5")
        self.lbl_expfile_outtype.grid(row=10, column=1, sticky="w", pady=(10, 0))

        self.combo_expfile_outtype = ttk.Combobox(self.main_frame, state="readonly", textvariable=self.var_expfile_outtype, values=['svg-fixed-pages', 'png-pages', 'pdf-svg-pages', 'pdf-png-pages', 'pdf-svg-merged', 'pdf-png-merged'])
        self.combo_expfile_outtype.current(4)
        self.combo_expfile_outtype.grid(row=11, column=1, columnspan=2, sticky="ew", padx=5)

        ### Output Type Extension Label
        self.chkbtn_expfile_outtypeext = tk.Checkbutton(self.main_frame, variable=self.var_expfile_outtypeext, bg="#f5f5f5")
        self.chkbtn_expfile_outtypeext.grid(row=11, column=3)

        ### Name Preview
        self.lbl_expfile_nameprev = tk.Label(self.main_frame, font=("Courier", 10, "italic"), fg="#666", bg="#f5f5f5")
        self.lbl_expfile_nameprev.grid(row=12, column=0, columnspan=4, sticky="w", pady=(5, 0))

        ## --- Export Button ---
        self.btn_export = tk.Button(self.main_frame, command=self.export_start, bg="#4caf50", fg="white", font=("Arial", 12, "bold"), height=2)
        self.btn_export.grid(row=13, column=0, columnspan=4, sticky="ew", pady=30)

        ## --- Links ---
        ### Link to Repo
        self.link_repo = tk.Label(self.main_frame, fg="#0056b3", bg="#f5f5f5", cursor="hand2", font=("Arial", 8, "underline"))
        self.link_repo.grid(row=14, column=0, sticky="w")
        self.link_repo.bind("<Button-1>", lambda a: webbrowser.open_new("https://github.com/MikeCat2008/smartboard-notebook-exporter"))

        ### Link to License
        self.link_license = tk.Label(self.main_frame, fg="#0056b3", bg="#f5f5f5", cursor="hand2", font=("Arial", 8, "underline"))
        self.link_license.grid(row=15, column=0, sticky="w")
        self.link_license.bind("<Button-1>", lambda a: webbrowser.open_new("https://www.gnu.org/licenses/gpl-3.0.html"))

        ### ANUNCIO 1 !¿?!¿?!¿?!¿?!¿!?!'¡!¿?!?¿!?¿¿?!?¿!?!¿!¿?¿?
        self.anuncio_1 = tk.Label(self.main_frame, fg="#0056b3", bg="#f5f5f5", cursor="hand2", font=("Arial", 8, "underline"))
        self.anuncio_1.grid(row=16, column=0, sticky="ew")
        self.anuncio_1.bind("<Button-1>", lambda a: webbrowser.open_new("https://media.tenor.com/Gi2zoa_JE5cAAAAj/locuraaaaaaaa-gato-lengua.gif"))

        ### ANUNCIO 2 - ahora si
        ad_img_1 = ImageTk.PhotoImage(Image.open(SRC_PATH+'imgs/Gemini_Generated_Image_1.jpeg').resize((567,100), Image.Resampling.LANCZOS))
        self.anuncio_2 = tk.Label(self.main_frame, image=ad_img_1, cursor="hand2")
        self.anuncio_2.image = ad_img_1
        self.anuncio_2.grid(row=4,column=0, columnspan=4, sticky="w")
        self.anuncio_2.bind("<Button-1>", lambda a: webbrowser.open_new("https://www.youtube.com/watch?v=jM7Vzzkz8z0"))
        

        ### ANUNCIO 3 - ahora tambien
        ad_img_2 = ImageTk.PhotoImage(Image.open(SRC_PATH+'imgs/Gemini_Generated_Image_2.jpeg').resize((167,760), Image.Resampling.LANCZOS))
        self.anuncio_3 = tk.Label(self.main_frame, image=ad_img_2, cursor="hand2")
        self.anuncio_3.image = ad_img_2
        self.anuncio_3.grid(row=1,column=4, rowspan=260, sticky="w")
        self.anuncio_3.bind("<Button-1>", lambda a: webbrowser.open_new("https://www.gentoo.org/get-involved/get-code/"))

        ### ANUNCIO 4 - puto copilot
        ad_img_3 = ImageTk.PhotoImage(Image.open(SRC_PATH+'imgs/anuncio.png').resize((300,210), Image.Resampling.LANCZOS))
        self.anuncio_4 = tk.Label(self.main_frame, image=ad_img_3, cursor='watch')
        self.anuncio_4.image = ad_img_3
        self.anuncio_4.grid(row=17,column=1, columnspan=3, sticky="ew")
        self.anuncio_4.bind("<Button-1>", lambda a: webbrowser.open_new("https://www.youtube.com/watch?v=s1EASMvoDXc"))

        ### ANUNCIO 5 - ahora no

        self.test = tk.Label(self.main_frame, font=("Arial", 14))
        self.test.grid(row=17,column=0, sticky="w")

        self.update_texts()

    # --- FUNCIONS ---
    ## --- Help ---
    def help1_tuto(self):
        self.var_help1_active = True

        self.btn_help1_tuto.grid_forget()
        self.btn_help2_outtypes.grid_forget()

        self.lbl_help1_page.grid(row=1, column=0, sticky="w", pady=(0,5))
        self.lbl_help1_page.config(text=self.gettext("lbl_help1_pages")[self.var_help1_pindex - 1])
        self.frame_help1_pcntl.grid(row=2,column=0, sticky="w")
        self.lbl_help1_pindex.grid(row=0, column=0, padx=(10,10))
        self.lbl_help1_pindex.config(text=f"{self.var_help1_pindex}/{self.var_help1_page_max}")
        self.btn_help1_prev.grid(row=0, column=1)
        if self.var_help1_pindex > self.var_help1_page_min:
            self.btn_help1_prev.config(state="normal")
        self.btn_help1_next.grid(row=0, column=2)
        if self.var_help1_pindex < self.var_help1_page_max:
            self.btn_help1_next.config(state="normal")
        self.btn_help1_exit.grid(row=0, column=3, padx=(10,0))

        if self.var_help1_pindex == 1:
            self.help1_shades(1,1,1,1,1,1,1,1,1)
        if self.var_help1_pindex == 2:
            self.help1_shades(0,1,1,1,1,1,1,1,1)
        if self.var_help1_pindex == 3:
            self.help1_shades(0,0,1,1,1,1,1,1,1)
        if self.var_help1_pindex == 4:
            self.help1_shades(1,1,0,1,1,1,1,1,1)
        if self.var_help1_pindex == 5:
            self.help1_shades(1,1,0,0,1,1,1,1,1)
        if self.var_help1_pindex == 6:
            self.help1_shades(1,1,0,1,0,1,1,1,1)
        if self.var_help1_pindex == 7:
            self.help1_shades(1,1,0,1,1,0,1,1,1)
        if self.var_help1_pindex == 8:
            self.help1_shades(1,1,0,1,1,1,0,1,1)
        if self.var_help1_pindex == 9:
            self.help1_shades(1,1,0,1,1,1,1,0,1)
        if self.var_help1_pindex == 10:
            self.help1_shades(1,1,1,1,1,1,1,1,0)
        if self.var_help1_pindex == 11:
            self.help1_shades(1,1,1,1,1,1,1,1,1)

        self.update_texts()

    def help1_shades(self, lbl_nbfile, nb_block, lbl_expfile, expfile_outdir_block, expfile_name_block, expfile_outtype_block, expfile_outtypeext, expfile_nameprev, btn_export):
        # send smth that evaluates to True (1) for disabled shade
        # send smth that evaluates to False (0) for normal shade

        if lbl_nbfile:
            self.lbl_nbfile.config(fg="#a3a3a3")
        else:
            self.lbl_nbfile.config(fg="#000000")

        if nb_block:
            self.ent_nbfile.config(state="disabled")
            self.btn_nbfile_browse.config(state="disabled")
        else:
            self.ent_nbfile.config(state="normal")
            self.btn_nbfile_browse.config(state="normal")

        if lbl_expfile:
            self.lbl_expfile.config(fg="#a3a3a3")
        else:
            self.lbl_expfile.config(fg="#000000")

        if expfile_outdir_block:
            self.lbl_expfile_outdir.config(fg="#a3a3a3")
            self.ent_expfile_outdir.config(state="disabled")
            self.btn_expfile_outdir.config(state="disabled")
        else:
            self.lbl_expfile_outdir.config(fg="#000000")
            self.ent_expfile_outdir.config(state="normal")
            self.btn_expfile_outdir.config(state="normal")

        if expfile_name_block:
            self.lbl_expfile_name.config(fg="#a3a3a3")
            self.ent_expfile_name.config(state="disabled")
        else:
            self.lbl_expfile_name.config(fg="#000000")
            self.ent_expfile_name.config(state="normal")

        if expfile_outtype_block:
            self.lbl_expfile_outtype.config(fg="#a3a3a3")
            self.combo_expfile_outtype.config(state="disabled")
        else:
            self.lbl_expfile_outtype.config(fg="#000000")
            self.combo_expfile_outtype.config(state="normal")

        if expfile_outtypeext:
            self.chkbtn_expfile_outtypeext.config(state="disabled")
        else:
            self.chkbtn_expfile_outtypeext.config(state="normal")

        if expfile_nameprev:
            self.lbl_expfile_nameprev.config(fg="#cacaca")
        else:
            self.lbl_expfile_nameprev.config(fg="#666")

        if btn_export:
            self.btn_export.config(state="disabled", fg="#a3a3a3", bg="#649666")
        else:
            self.btn_export.config(state="normal", fg="#ffffff", bg="#4caf50")


    def help1_tuto_pages(self, sum_type):
        if sum_type:
            if self.var_help1_pindex >= self.var_help1_page_max:
                self.btn_help1_next.config(state="disabled")
            else:
                self.var_help1_pindex += 1
        else:
            if self.var_help1_pindex <= self.var_help1_page_min:
                self.btn_help1_prev.config(state="disabled")
            else:
                self.var_help1_pindex -= 1
        if self.var_help1_pindex > self.var_help1_page_min:
            self.btn_help1_prev.config(state="normal")
        if self.var_help1_pindex < self.var_help1_page_max:
            self.btn_help1_next.config(state="normal")
        if self.var_help1_pindex >= self.var_help1_page_max:
            self.btn_help1_next.config(state="disabled")
        if self.var_help1_pindex <= self.var_help1_page_min:
            self.btn_help1_prev.config(state="disabled")

        if self.var_help1_pindex == 1:
            self.help1_shades(1,1,1,1,1,1,1,1,1)
        if self.var_help1_pindex == 2:
            self.help1_shades(0,1,1,1,1,1,1,1,1)
        if self.var_help1_pindex == 3:
            self.help1_shades(0,0,1,1,1,1,1,1,1)
        if self.var_help1_pindex == 4:
            self.help1_shades(1,1,0,1,1,1,1,1,1)
        if self.var_help1_pindex == 5:
            self.help1_shades(1,1,0,0,1,1,1,1,1)
        if self.var_help1_pindex == 6:
            self.help1_shades(1,1,0,1,0,1,1,1,1)
        if self.var_help1_pindex == 7:
            self.help1_shades(1,1,0,1,1,0,1,1,1)
        if self.var_help1_pindex == 8:
            self.help1_shades(1,1,0,1,1,1,0,1,1)
        if self.var_help1_pindex == 9:
            self.help1_shades(1,1,0,1,1,1,1,0,1)
        if self.var_help1_pindex == 10:
            self.help1_shades(1,1,1,1,1,1,1,1,0)
        if self.var_help1_pindex == 11:
            self.help1_shades(1,1,1,1,1,1,1,1,1)

        self.lbl_help1_page.config(text=self.gettext("lbl_help1_pages")[self.var_help1_pindex - 1])
        self.lbl_help1_pindex.config(text=f"{self.var_help1_pindex}/{self.var_help1_page_max}")

    def help1_tuto_exit(self):
        self.var_help1_active = False

        self.btn_help1_tuto.grid(row=1, column=0, sticky="w", padx=(0,10))
        self.btn_help2_outtypes.grid(row=1, column=1, sticky="w")

        self.lbl_help1_page.grid_forget()
        self.frame_help1_pcntl.grid_forget()

        self.help1_shades(0,0,0,0,0,0,0,0,0)
        self.update_texts()

    def help2_outtypes(self):
        self.var_help2_active = True

        self.btn_help1_tuto.grid_forget()
        self.btn_help2_outtypes.grid_forget()

        self.lbl_help2_page.grid(row=1, column=0, sticky="w", pady=(0,5))
        self.lbl_help2_page.config(text=self.gettext("lbl_help2_pages")[self.var_help2_pindex - 1])
        self.frame_help2_pcntl.grid(row=2,column=0, sticky="w")
        self.lbl_help2_pindex.grid(row=0, column=0, padx=(10,10))
        self.lbl_help2_pindex.config(text=f"{self.var_help2_pindex}/{self.var_help2_page_max}")
        self.btn_help2_prev.grid(row=0, column=1)
        if self.var_help2_pindex > self.var_help2_page_min:
            self.btn_help2_prev.config(state="normal")
        self.btn_help2_next.grid(row=0, column=2)
        if self.var_help2_pindex < self.var_help2_page_max:
            self.btn_help2_next.config(state="normal")
        self.btn_help2_exit.grid(row=0, column=3, padx=(10,0))

        self.update_texts()

    def help2_outtypes_pages(self, sum_type):
        if sum_type:
            if self.var_help2_pindex >= self.var_help2_page_max:
                self.btn_help2_next.config(state="disabled")
            else:
                self.var_help2_pindex += 1
        else:
            if self.var_help2_pindex <= self.var_help2_page_min:
                self.btn_help2_prev.config(state="disabled")
            else:
                self.var_help2_pindex -= 1
        if self.var_help2_pindex > self.var_help2_page_min:
            self.btn_help2_prev.config(state="normal")
        if self.var_help2_pindex < self.var_help2_page_max:
            self.btn_help2_next.config(state="normal")
        if self.var_help2_pindex >= self.var_help2_page_max:
            self.btn_help2_next.config(state="disabled")
        if self.var_help2_pindex <= self.var_help2_page_min:
            self.btn_help2_prev.config(state="disabled")

        self.lbl_help2_page.config(text=self.gettext("lbl_help2_pages")[self.var_help2_pindex - 1])
        self.lbl_help2_pindex.config(text=f"{self.var_help2_pindex}/{self.var_help2_page_max}")

    def help2_outtypes_exit(self):
        self.var_help2_active = False

        self.btn_help1_tuto.grid(row=1, column=0, sticky="w", padx=(0,10))
        self.btn_help2_outtypes.grid(row=1, column=1, sticky="w")

        self.lbl_help2_page.grid_forget()
        self.frame_help2_pcntl.grid_forget()

        self.update_texts()

    ## ---
    def nbfile_search(self):
        filename = filedialog.askopenfilename(filetypes=[("Smartboard notebook","*.notebook")])
        if filename:
            self.ent_nbfile.delete(0, tk.END)
            self.ent_nbfile.insert(0, filename)

    def expfile_outfold_search(self):
        directory = filedialog.askdirectory()
        if directory:
            self.ent_expfile_outdir.delete(0, tk.END)
            self.ent_expfile_outdir.insert(0, directory)

    def expfile_nameprev_update(self, *args):
        if self.var_expfile_name.get():
            name = self.var_expfile_name.get()
        elif self.var_nbfile.get():
            name = Path(self.var_nbfile.get()).stem
        else:
            name = "my_file"
        outtype = self.var_expfile_outtype.get()
        outtype_ext_map = {
            'svg-fixed-pages': 'zip',
            'png-pages': 'zip',
            'pdf-svg-pages': 'zip',
            'pdf-png-pages': 'zip',
            'pdf-svg-merged': 'pdf',
            'pdf-png-merged': 'pdf',

            'hola' : 'zip',
            'endogamia': 'zip',
            'parafilia': 'zip',
            'tungsteno': 'zip',
            'cloroformo': 'pdf',
            'estrogeno': 'pdf'
        }
        ext = outtype_ext_map.get(outtype, "ext")
        if self.var_expfile_outtypeext.get():
            self.var_expfile_nameprev = f"{name}_{outtype}.{ext}"
        else:
            self.var_expfile_nameprev = f"{name}.{ext}"
        self.update_texts()

    def fileoverwrite_check(self):
        if self.var_expfile_outdir.get():
            export_path = Path(self.var_expfile_outdir.get()).resolve()
        else:
            export_path = Path(self.var_nbfile.get()).resolve().parent

        self.expfile_nameprev_update()

        if Path(export_path, self.var_expfile_nameprev).is_file():
            return True
        else:
            return False

    ## --- Export ---
    def export_enable(self):
        self.var_export_active.set(False)
        self.btn_export.config(bg="#4caf50", state="normal")
        self.update_texts()

    def export_start(self):
        self.var_export_active.set(True)
        self.btn_export.config(bg="#af4c50", state="disabled")
        self.update_texts()

        self.root.update() # Force UI Rendering
        self.export_process()

    def export_process(self):
        infile = self.var_nbfile.get().strip()
        export_type = self.gettext("export_types").get(self.var_expfile_outtype.get())
        export_path = self.var_expfile_outdir.get().strip()  # If empty ""
        export_name = self.var_expfile_name.get().strip() # If empty: ""
        otnextension_bool = self.var_expfile_outtypeext.get()

        if not infile:
            tk.messagebox.Message(
                icon="warning",
                type="ok",
                message=self.gettext("msgbox_warn_missfile_msg"),
                detail=self.gettext("msgbox_warn_missfile_dtl")
            ).show()
            self.export_enable()
            return

        if self.fileoverwrite_check():
            fileoverwrite_answer = tk.messagebox.askyesno(
                icon="warning",
                message=self.gettext("msgbox_warn_fileow_msg"),
                detail=self.gettext("msgbox_warn_fileow_dtl")
            )
            self.root.update() # Force UI Rendering
            if not fileoverwrite_answer:
                self.export_enable()
                return

        try:
            main.main(infile, export_type, export_path, export_name, otnextension_bool)
            tk.messagebox.Message(
                icon="info",
                type="ok",
                message=self.gettext("msgbox_info_ok_msg"),
                detail=self.gettext("msgbox_info_ok_dtl")
            ).show()
            self.export_enable()
        except Exception as e:
            tk.messagebox.Message(
                icon="error",
                type="ok",
                message=self.gettext("msgbox_err_exp_msg"),
                detail=f"{self.gettext("msgbox_err_exp_dtl")}\n{e}"
            ).show()
            self.export_enable()

    ## --- i18n ---
    def set_lang(self, langkey):
        self.var_lang = langkey
        self.update_texts()

    def gettext(self, textkey):
        return gui_locales.locales[self.var_lang].get(textkey, textkey)

    def update_texts(self):
        self.ntbk_confhelp.tab(self.confhelp_tab3_help, text=self.gettext("lbl_help"))
        self.lbl_help.config(text=self.gettext("lbl_help"))
        self.ntbk_confhelp.tab(self.confhelp_tab2_ver, text=self.gettext("lbl_ver"))
        self.lbl_ver.config(text=self.gettext("lbl_ver"))
        self.lbl_ver_curtxt.config(text=self.gettext("lbl_ver_curtxt"))
        self.btn_ver_chkupd.config(text=self.gettext("btn_ver_chkupd"))
        self.ntbk_confhelp.tab(self.confhelp_tab1_i18n, text=self.gettext("lbl_lang"))
        self.lbl_lang.config(text=self.gettext("lbl_lang"))
        self.lbl_lang_info.config(text=self.gettext("lbl_lang_info"))
        self.lbl_nbfile.config(text=self.gettext("lbl_nbfile"))
        self.btn_nbfile_browse.config(text=self.gettext("btn_nbfile_browse"))
        self.lbl_expfile.config(text=self.gettext("lbl_expfile"))
        self.lbl_expfile_outdir.config(text=self.gettext("lbl_expfile_outdir"))
        self.btn_expfile_outdir.config(text=self.gettext("btn_expfile_outdir"))
        self.lbl_expfile_name.config(text=self.gettext("lbl_expfile_name"))
        self.lbl_expfile_outtype.config(text=self.gettext("lbl_expfile_outtype"))
        self.chkbtn_expfile_outtypeext.config(text=self.gettext("chkbtn_expfile_outtypeext"))
        self.lbl_expfile_nameprev.config(text=f"{self.gettext("lbl_expfile_nameprev")} {self.var_expfile_nameprev}")
        if self.var_export_active.get():
            self.btn_export.config(text=self.gettext("btn_export_active"))
        else:
            self.btn_export.config(text=self.gettext("btn_export"))
        self.link_repo.config(text=self.gettext("link_repo"))
        self.link_license.config(text=self.gettext("link_license"))

        if self.var_help1_active:
            self.lbl_help1_page.config(text=self.gettext("lbl_help1_pages")[self.var_help1_pindex - 1])
            self.btn_help1_exit.config(text=self.gettext("btn_help_exit"))
        elif self.var_help2_active:
            self.lbl_help2_page.config(text=self.gettext("lbl_help2_pages")[self.var_help2_pindex - 1])
            self.btn_help2_exit.config(text=self.gettext("btn_help_exit"))
        else:
            self.btn_help1_tuto.config(text=self.gettext("btn_help1_tuto"))
            self.btn_help2_outtypes.config(text=self.gettext("btn_help2_outtypes"))

        self.test.config(text=self.gettext("test"))
        self.anuncio_1.config(text=self.gettext("anuncio_1"))

        remember_bro = self.combo_expfile_outtype['values'].index(self.combo_expfile_outtype.get())
        self.combo_expfile_outtype['values'] = list(self.gettext("export_types").keys())
        self.combo_expfile_outtype.current(remember_bro)
            

if __name__ == "__main__":
    root = tk.Tk()
    app = ExporterApp(root)
    root.mainloop()
