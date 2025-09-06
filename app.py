"""Tkinter UI for the password generator.

Launch this module to run the GUI: `python app.py`.
"""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox

from generator import generate_password


class PasswordApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Password Generator")
        self.resizable(False, False)

        # Length
        frm_len = tk.Frame(self)
        frm_len.grid(row=0, column=0, padx=8, pady=(10, 4), sticky="ew")
        tk.Label(frm_len, text="Password Length:").grid(row=0, column=0, sticky="w")
        self.entry_length = tk.Entry(frm_len, width=8)
        self.entry_length.insert(0, "12")
        self.entry_length.grid(row=0, column=1, padx=(6, 0))

        # Options
        frm_opts = tk.LabelFrame(self, text="Character Sets")
        frm_opts.grid(row=1, column=0, padx=8, pady=4, sticky="ew")
        self.var_lower = tk.BooleanVar(value=True)
        self.var_upper = tk.BooleanVar(value=True)
        self.var_digits = tk.BooleanVar(value=True)
        self.var_special = tk.BooleanVar(value=True)
        tk.Checkbutton(frm_opts, text="Lowercase", variable=self.var_lower).grid(row=0, column=0, sticky="w", padx=6, pady=2)
        tk.Checkbutton(frm_opts, text="Uppercase", variable=self.var_upper).grid(row=0, column=1, sticky="w", padx=6, pady=2)
        tk.Checkbutton(frm_opts, text="Digits", variable=self.var_digits).grid(row=1, column=0, sticky="w", padx=6, pady=2)
        tk.Checkbutton(frm_opts, text="Special", variable=self.var_special).grid(row=1, column=1, sticky="w", padx=6, pady=2)

        # Actions
        frm_actions = tk.Frame(self)
        frm_actions.grid(row=2, column=0, padx=8, pady=6, sticky="ew")
        btn_gen = tk.Button(frm_actions, text="Generate", command=self.on_generate)
        btn_gen.grid(row=0, column=0, padx=(0, 6))
        btn_copy = tk.Button(frm_actions, text="Copy", command=self.on_copy)
        btn_copy.grid(row=0, column=1)

        # Result
        frm_res = tk.Frame(self)
        frm_res.grid(row=3, column=0, padx=8, pady=(0, 10), sticky="ew")
        tk.Label(frm_res, text="Generated Password:").grid(row=0, column=0, sticky="w")
        self.entry_result = tk.Entry(frm_res, width=32)
        self.entry_result.grid(row=0, column=1, padx=(6, 0))

    def on_generate(self) -> None:
        try:
            length_str = self.entry_length.get().strip()
            length = int(length_str)
            if length <= 0:
                raise ValueError("Length must be positive.")

            pwd = generate_password(
                length=length,
                use_lower=self.var_lower.get(),
                use_upper=self.var_upper.get(),
                use_digits=self.var_digits.get(),
                use_special=self.var_special.get(),
            )
            self.entry_result.delete(0, tk.END)
            self.entry_result.insert(0, pwd)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def on_copy(self) -> None:
        value = self.entry_result.get()
        if not value:
            messagebox.showinfo("Copy", "Nothing to copy yet.")
            return
        self.clipboard_clear()
        self.clipboard_append(value)
        self.update()  # ensure clipboard is updated
        messagebox.showinfo("Copy", "Password copied to clipboard.")


def main() -> None:
    app = PasswordApp()
    app.mainloop()


if __name__ == "__main__":
    main()
