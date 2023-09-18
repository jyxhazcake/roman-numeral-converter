import tkinter as tk
from tkinter import font, messagebox

class Interface(tk.Frame):
    def __init__(self, master, title, converter, result_prefix):
        super().__init__(master, padx=20, pady=10)
        self.converter = converter
        self.result_prefix = result_prefix

        # Fonts
        title_font = font.Font(family="Times",size=14)
        label_font = font.Font(family="Times",size=12)
        result_font = font.Font(family="Times",size=13, weight="bold")

        # Label
        self.label = tk.Label(self, text=title, font=title_font)
        self.label.grid(row=0, column=0, pady=10)

        # Input
        self.entry = tk.Entry(self, width=20, font=label_font)
        self.entry.grid(row=1, column=0, pady=5)

        # Button
        self.convert_button = tk.Button(self, text="Convert", command=self.perform_conversion, font=label_font)
        self.convert_button.grid(row=2, column=0, pady=5)

        # Result
        self.result_label = tk.Label(self, text="", font=result_font)
        self.result_label.grid(row=3, column=0, pady=5)

    def perform_conversion(self):
        value = self.entry.get()
        try:
            result = self.converter.convert(value)
            self.result_label.config(text=f"{self.result_prefix}: {result}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
