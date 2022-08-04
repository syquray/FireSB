import os
import tkinter as tk
from tkinter import filedialog, ttk


class MainWindow(tk.Frame):
    def __init__(self, width: int, height: int, title: str) -> None:
        self.root = tk.Tk()
        super().__init__(self.root)

        self.file_name = tk.StringVar()
        self.file_name.set("未選択")

        sw, sh = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        w, h = width, height

        self.root.title(title)
        self.root.geometry(f"{w}x{h}+{int(sw/2-w/2)}+{int(sh/2-h/2)}")

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.set_button("参照...", 40, self.open_file)
        self.set_label(0, self.file_name)

        self.run()

    def run(self) -> None:
        self._update()
        self.root.mainloop()

    def _update(self) -> None:
        self.root.update_idletasks()

    def close(self) -> None:
        self.root.destroy()

    def open_file(self, event) -> None:
        f_type = [("Scratch プロジェクトファイル", "*.sb3")]
        i_dir = os.path.abspath(os.path.dirname(__file__))
        file_name = filedialog.askopenfilename(filetypes=f_type, initialdir=i_dir)

        if not len(file_name) == 0:
            self.file_name.set(file_name)

    def set_label(self, pad_y: int, text_var) -> None:
        label = ttk.Label(self.frame, textvariable=text_var)
        label.pack(pady=pad_y)

    def set_button(self, text: str, pad_y: int, handler) -> None:
        button = ttk.Button(self.frame, text=text)
        button.bind("<ButtonPress>", handler)
        button.pack(pady=pad_y)
