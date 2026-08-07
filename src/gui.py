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

import gui_locales
import main

import tkinter as tk
from tkinter import ttk, filedialog

import webbrowser

from pathlib import Path

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

        # --- VISUAL ELEMENTS LAYOUT ---
        self.main_frame = tk.Frame(root, bg="#f5f5f5", padx=20, pady=20)
        self.main_frame.pack()

        ## --- App Name ---
        tk.Label(self.main_frame, text="Smartboard notebook Exporter", font=("Arial", 20, "bold"), bg="#f5f5f5", fg="#333").grid(row=0, column=0, columnspan=4, pady=(0, 10))

        ttk.Separator(self.main_frame, orient='horizontal').grid(row=1, column=0, columnspan=4, sticky="ew", pady=(0, 10))

        ## --- Version Section ---
        self.lbl_ver = tk.Label(self.main_frame, font=("Arial", 12, "bold"), bg="#f5f5f5")
        self.lbl_ver.grid(row=2, column=0, columnspan=2, sticky="w", padx=(0,10))

        self.lbl_ver_curtxt = tk.Label(self.main_frame, font=("Arial", 10), bg="#f5f5f5")
        self.lbl_ver_curtxt.grid(row=3, column=0, sticky="w")

        self.lbl_ver_cur = tk.Label(self.main_frame, text="v1.1.0", font=("Arial", 10, "bold"), bg="#f5f5f5")
        self.lbl_ver_cur.grid(row=3, column=1, sticky="e", padx=(0,10))

        self.btn_ver_chkupd = tk.Button(self.main_frame, command=lambda: webbrowser.open_new("https://github.com/MikeCat2008/smartboard-notebook-exporter/releases/latest"))
        self.btn_ver_chkupd.grid(row=4, column=0, columnspan=2, sticky="ew", padx=(0,10))

        ## --- i18n Section ---
        self.lbl_lang = tk.Label(self.main_frame, font=("Arial", 12, "bold"), bg="#f5f5f5")
        self.lbl_lang.grid(row=2, column=2, columnspan=2, sticky="w")

        self.lbl_lang_info = tk.Label(self.main_frame, font=("Arial", 10), bg="#f5f5f5")
        self.lbl_lang_info.grid(row=3, column=2, sticky="w")

        self.frame_lang = tk.Frame(self.main_frame, bg="#f5f5f5")
        self.frame_lang.grid(row=4, rowspan=2, column=2, columnspan=2, sticky="w")

        self.btn_lang_es = tk.Button(self.frame_lang, text="ES", width="3", command=lambda: self.set_lang("es"))
        self.btn_lang_es.grid(row=1, column=0, sticky="w", padx=(0, 5))

        self.btn_lang_en = tk.Button(self.frame_lang, text="EN", width="3", command=lambda: self.set_lang("en"))
        self.btn_lang_en.grid(row=1, column=1, sticky="w", padx=(0, 5))

        ttk.Separator(self.main_frame, orient='horizontal').grid(row=6, column=0, columnspan=4, sticky="ew", pady=(10, 10))

        ## --- Notebook File Section ---
        self.lbl_nbfile = tk.Label(self.main_frame, font=("Arial", 14, "bold"), bg="#f5f5f5")
        self.lbl_nbfile.grid(row=7, column=0, sticky="w")

        self.ent_nbfile = tk.Entry(self.main_frame, textvariable=self.var_nbfile, width=40)
        self.ent_nbfile.grid(row=8, column=0, columnspan=3, sticky="ew", padx=(0, 10), pady=10)

        self.btn_nbfile_browse = tk.Button(self.main_frame, command=self.nbfile_search)
        self.btn_nbfile_browse.grid(row=8, column=3, sticky="ew")

        ## --- Export File Section ---
        self.lbl_expfile = tk.Label(self.main_frame, font=("Arial", 14, "bold"), bg="#f5f5f5")
        self.lbl_expfile.grid(row=9, column=0, sticky="w", pady=(20, 5))

        ### Output Directory
        self.lbl_expfile_outdir = tk.Label(self.main_frame, font=("Arial", 10), bg="#f5f5f5")
        self.lbl_expfile_outdir.grid(row=10, column=0, sticky="w")

        self.ent_expfile_outdir = tk.Entry(self.main_frame, textvariable=self.var_expfile_outdir)
        self.ent_expfile_outdir.grid(row=11, column=0, columnspan=3, sticky="ew", padx=(0, 10), pady=5)

        self.btn_expfile_outdir = tk.Button(self.main_frame, command=self.expfile_outfold_search)
        self.btn_expfile_outdir.grid(row=11, column=3, sticky="ew")

        ### Custom Name
        self.lbl_expfile_name = tk.Label(self.main_frame, font=("Arial", 10), bg="#f5f5f5")
        self.lbl_expfile_name.grid(row=12, column=0, sticky="w", pady=(10, 0))

        self.ent_expfile_name = tk.Entry(self.main_frame, textvariable=self.var_expfile_name)
        self.ent_expfile_name.grid(row=13, column=0, sticky="ew", padx=(0, 5))

        ### Output Type
        self.lbl_expfile_outtype = tk.Label(self.main_frame, font=("Arial", 10), bg="#f5f5f5")
        self.lbl_expfile_outtype.grid(row=12, column=1, sticky="w", pady=(10, 0))

        self.combo_expfile_outtype = ttk.Combobox(self.main_frame, state="readonly", textvariable=self.var_expfile_outtype, values=['svg-fixed-pages', 'png-pages', 'pdf-svg-pages', 'pdf-png-pages', 'pdf-svg-merged', 'pdf-png-merged'])
        self.combo_expfile_outtype.current(4)
        self.combo_expfile_outtype.grid(row=13, column=1, columnspan=2, sticky="ew", padx=5)

        ### Output Type Extension Label
        self.chkbtn_expfile_outtypeext = tk.Checkbutton(self.main_frame, variable=self.var_expfile_outtypeext, bg="#f5f5f5")
        self.chkbtn_expfile_outtypeext.grid(row=13, column=3)

        ### Name Preview
        self.lbl_expfile_nameprev = tk.Label(self.main_frame, font=("Courier", 10, "italic"), fg="#666", bg="#f5f5f5")
        self.lbl_expfile_nameprev.grid(row=14, column=0, columnspan=4, sticky="w", pady=(5, 0))

        ## --- Export Button ---
        self.btn_export = tk.Button(self.main_frame, command=self.export_start, bg="#4caf50", fg="white", font=("Arial", 12, "bold"), height=2)
        self.btn_export.grid(row=15, column=0, columnspan=4, sticky="ew", pady=30)

        ## --- Links ---
        ### Link to Repo
        self.link_repo = tk.Label(self.main_frame, fg="#0056b3", bg="#f5f5f5", cursor="hand2", font=("Arial", 8, "underline"))
        self.link_repo.grid(row=16, column=0, sticky="w")
        self.link_repo.bind("<Button-1>", lambda a: webbrowser.open_new("https://github.com/MikeCat2008/smartboard-notebook-exporter"))

        ### Link to License
        self.link_license = tk.Label(self.main_frame, fg="#0056b3", bg="#f5f5f5", cursor="hand2", font=("Arial", 8, "underline"))
        self.link_license.grid(row=17, column=0, sticky="w")
        self.link_license.bind("<Button-1>", lambda a: webbrowser.open_new("https://www.gnu.org/licenses/gpl-3.0.html"))

        #self.test = tk.Label(root, font=("Arial", 14))
        #self.test.pack()

        self.update_texts()

    # --- FUNCIONS ---
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
            'pdf-png-merged': 'pdf'
        }
        ext = outtype_ext_map.get(outtype, "ext")
        if self.var_expfile_outtypeext.get():
            self.var_expfile_nameprev = f"{name}_{outtype}.{ext}"
        else:
            self.var_expfile_nameprev = f"{name}.{ext}"
        self.update_texts()

    ## --- Export ---
    def export_enable(self):
        self.var_export_active.set(False)
        self.btn_export.config(bg="#4caf50", state="normal")
        self.update_texts()

    def export_start(self):
        self.var_export_active.set(True)
        self.btn_export.config(bg="#af4c50", state="disabled")
        self.update_texts()

        # 50ms for UI Rendering before export_process
        self.btn_export.after(50, self.export_process)

    def export_process(self):
        infile = self.var_nbfile.get().strip()
        export_type = self.var_expfile_outtype.get()
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
        self.lbl_ver.config(text=self.gettext("lbl_ver"))
        self.lbl_ver_curtxt.config(text=self.gettext("lbl_ver_curtxt"))
        self.btn_ver_chkupd.config(text=self.gettext("btn_ver_chkupd"))
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

        #self.test.config(text=self.gettext("test"))

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("650x650")
    app = ExporterApp(root)
    root.mainloop()
