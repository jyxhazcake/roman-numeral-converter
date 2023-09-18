import tkinter as tk
from interface import Interface
from converter import NumToRoman, RomanToNum

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Roman Numeral Converter")

        self.num_to_roman_frame = Interface(root, "Number to Roman", NumToRoman(), "Roman")
        self.num_to_roman_frame.pack(pady=20)

        self.roman_to_num_frame = Interface(root, "Roman to Number", RomanToNum(), "Number")
        self.roman_to_num_frame.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
