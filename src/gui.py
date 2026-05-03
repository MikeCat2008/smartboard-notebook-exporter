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

        self.extension_map = {
            'svg-fixed-pages': 'zip',
            'png-pages': 'zip',
            'pdf-svg-pages': 'zip',
            'pdf-png-pages': 'zip',
            'pdf-svg-merged': 'pdf',
            'pdf-png-merged': 'pdf'
        }
        self.full_name = None
        
        # ----- MAIN FRAME -----
        self.main_frame = tk.Frame(root, bg="#f5f5f5", padx=20, pady=20) # Margin for all the window
        self.main_frame.pack()

        # --- REACTIVE VARIABLES ---
        self.var_in_name = tk.StringVar(value="")
        self.var_out_name = tk.StringVar(value="")
        self.var_type = tk.StringVar()
        self.var_ext_toggle = tk.BooleanVar(value=True)

        # Search for changes for name preview
        self.var_out_name.trace_add("write", self.update_preview)
        self.var_in_name.trace_add("write", self.update_preview)
        self.var_type.trace_add("write", self.update_preview)
        self.var_ext_toggle.trace_add("write", self.update_preview)

        # --- TITLE ---
        tk.Label(self.main_frame, text="Smartboard notebook Exporter", font=("Arial", 20, "bold"), bg="#f5f5f5", fg="#333").grid(row=0, column=0, columnspan=4, pady=(0, 10))
        
        ttk.Separator(self.main_frame, orient='horizontal').grid(row=1, column=0, columnspan=4, sticky="ew", pady=(0, 20))

        # --- NOTEBOOK FILE ---
        tk.Label(self.main_frame, text="Notebook File", font=("Arial", 14, "bold"), bg="#f5f5f5").grid(row=2, column=0, sticky="w")
        
        self.ent_notebook = tk.Entry(self.main_frame, textvariable=self.var_in_name, width=40)
        self.ent_notebook.grid(row=3, column=0, columnspan=3, sticky="ew", padx=(0, 10), pady=10)
        
        tk.Button(self.main_frame, text="BROWSE", command=self.search_file).grid(row=3, column=3, sticky="ew")

        # --- EXPORT FILE ---
        tk.Label(self.main_frame, text="Export File", font=("Arial", 14, "bold"), bg="#f5f5f5").grid(row=4, column=0, sticky="w", pady=(20, 5))
        
        # Output Folder
        tk.Label(self.main_frame, text="Output Folder", font=("Arial", 10), bg="#f5f5f5").grid(row=5, column=0, sticky="w")
        self.ent_output = tk.Entry(self.main_frame)
        self.ent_output.grid(row=6, column=0, columnspan=3, sticky="ew", padx=(0, 10), pady=5)
        tk.Button(self.main_frame, text="BROWSE", command=self.search_dir).grid(row=6, column=3, sticky="ew")

        # Name and Type
        tk.Label(self.main_frame, text="Name (opt)", font=("Arial", 10), bg="#f5f5f5").grid(row=7, column=0, sticky="w", pady=(10, 0))
        tk.Label(self.main_frame, text="Output Type", font=("Arial", 10), bg="#f5f5f5").grid(row=7, column=1, sticky="w", pady=(10, 0))
        
        self.ent_name = tk.Entry(self.main_frame, textvariable=self.var_out_name)
        self.ent_name.grid(row=8, column=0, sticky="ew", padx=(0, 5))
        
        self.combo_type = ttk.Combobox(self.main_frame, state="readonly", textvariable=self.var_type, values=['svg-fixed-pages', 'png-pages', 'pdf-svg-pages', 'pdf-png-pages', 'pdf-svg-merged', 'pdf-png-merged'])
        self.combo_type.current(0)
        self.combo_type.grid(row=8, column=1, columnspan=2, sticky="ew", padx=5)
        
        tk.Checkbutton(self.main_frame, variable=self.var_ext_toggle, text="Extension Name Toggle", bg="#f5f5f5").grid(row=8, column=3)

        # --- PREVIEW LABEL ---
        self.lbl_preview = tk.Label(self.main_frame, text="", font=("Courier", 10, "italic"), fg="#666", bg="#f5f5f5")
        self.lbl_preview.grid(row=9, column=0, columnspan=4, sticky="w", pady=(5, 0))

        self.update_preview()

        # --- EXPORT ---
        self.btn_export = tk.Button(self.main_frame, text="EXPORT", command=self.export, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), height=2)
        self.btn_export.grid(row=10, column=0, columnspan=4, sticky="ew", pady=30)

        # --- LINKS ---
        # Link to Repo (Left)
        link_repo = tk.Label(self.main_frame, text="GitHub Repository", fg="#0056b3", bg="#f5f5f5", cursor="hand2", font=("Arial", 8, "underline"))
        link_repo.grid(row=11, column=0, sticky="w")
        link_repo.bind("<Button-1>", lambda a: webbrowser.open_new("https://github.com/MikeCat2008/smartboard-notebook-exporter"))

        # Link to License (Right)
        link_license = tk.Label(self.main_frame, text="GPLv3 License", fg="#0056b3", bg="#f5f5f5", cursor="hand2", font=("Arial", 8, "underline"))
        link_license.grid(row=12, column=0, sticky="w")
        link_license.bind("<Button-1>", lambda a: webbrowser.open_new("https://www.gnu.org/licenses/gpl-3.0.html"))

    def search_file(self):
        filename = filedialog.askopenfilename(filetypes=[("Smartboard notebook","*.notebook")])
        if filename:
            self.ent_notebook.delete(0, tk.END)
            self.ent_notebook.insert(0, filename)

    def search_dir(self):
        directory = filedialog.askdirectory()
        if directory:
            self.ent_output.delete(0, tk.END)
            self.ent_output.insert(0, directory)

    def update_preview(self, *args):
        if self.var_out_name.get():
            name = self.var_out_name.get()
        else:
            if self.var_in_name.get():
                name = Path(self.var_in_name.get()).stem
            else:
                name = "my_file"
        out_type = self.var_type.get()
        ext = self.extension_map[out_type]

        if self.var_ext_toggle.get():
            # Long format: file_pdf-svg-merged.pdf
            self.full_name = f"{name}_{out_type}.{ext}"
        else:
            # Short format: file.pdf
            self.full_name = f"{name}.{ext}"

        self.lbl_preview.config(text=f"Preview: {self.full_name}")

    def export(self):
        infile = self.var_in_name.get().strip()
        export_type = self.var_type.get()
        export_path = self.ent_output.get().strip()  # If empty ""
        export_name = self.var_out_name.get().strip() # If empty: ""
        otnextension_bool = self.var_ext_toggle.get()

        if not infile:
            tk.messagebox.showwarning("Remaining File", "Please, select a .notebook file first.")
            return

        try:
            main.main(infile, export_type, export_path, export_name, otnextension_bool)
            tk.messagebox.showinfo("Success!", f"Your file '{self.full_name}' has been successfuly exported.")
        except Exception as e:
            tk.messagebox.showwarning("Error",f"Something went wrong:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExporterApp(root)
    root.mainloop()
