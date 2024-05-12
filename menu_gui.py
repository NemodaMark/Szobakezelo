import tkinter as tk
import subprocess

def open_script(script_name):
    subprocess.run(["python", script_name])

def create_button(root, text, script_name, row):
    button = tk.Button(root, text=text, command=lambda script=script_name: open_script(script))
    button.grid(row=row, column=0, pady=5)
    return button

root = tk.Tk()
root.title("My Window")
root.geometry("300x200")
root.config(padx=10, pady=10)

title_label = tk.Label(root, text="Szobakezelő", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, pady=10)

buttons = [
    {"text": "Foglalás", "script": "claim_gui.py"},
    {"text": "Lemondás", "script": "resign_gui.py"},
    {"text": "Listázás", "script": "all_gui.py"},
]

for i, button_config in enumerate(buttons):
    create_button(root, button_config["text"], button_config["script"], i + 1)

root.mainloop()