import os
import zipfile
import tkinter as tk
from tkinter import filedialog

class WHLExtractor:
    def __init__(self, master):
        self.master = master
        master.title("WHL Extractor")

        # Label for displaying information
        self.info_label = tk.Label(master, text="")
        self.info_label.pack(pady=10)

        # Button to select WHL file
        self.select_whl_button = tk.Button(master, text="Select WHL File", command=self.select_whl_file)
        self.select_whl_button.pack(pady=5)

        # Button to select extraction path
        self.select_extract_button = tk.Button(master, text="Select Extraction Path", command=self.select_extraction_path)
        self.select_extract_button.pack(pady=5)

        # Button to start extraction
        self.extract_button = tk.Button(master, text="Extract", command=self.extract_whl)
        self.extract_button.pack(pady=10)

        # Initialize variables
        self.whl_path = ""
        self.extract_path = ""

    def select_whl_file(self):
        self.whl_path = filedialog.askopenfilename(filetypes=[("WHL files", "*.whl")])
        self.info_label.config(text=f"Selected WHL file: {self.whl_path}")

    def select_extraction_path(self):
        self.extract_path = filedialog.askdirectory()
        self.info_label.config(text=f"Selected extraction path: {self.extract_path}")

    def extract_whl(self):
        if not self.whl_path or not self.extract_path:
            self.info_label.config(text="Please select both WHL file and extraction path.")
            return

        try:
            with zipfile.ZipFile(self.whl_path, 'r') as zip_ref:
                zip_ref.extractall(self.extract_path)
            self.info_label.config(text=f"Extraction successful. Files extracted to: {self.extract_path}")
        except zipfile.BadZipFile:
            self.info_label.config(text="Error: Not a valid WHL file.")
        except Exception as e:
            self.info_label.config(text=f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WHLExtractor(root)
    root.mainloop()
