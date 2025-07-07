import tkinter as tk
from tkinter import messagebox
import gui_test  # This assumes your main GUI file is named gui.py

def verify_password():
    entered = entry.get()
    if entered == MASTER_PASSWORD:
        root.destroy()
        gui_test()  # This launches your main GUI
    else:
        messagebox.showerror("Access Denied", "Incorrect master password.")

# You can change this to whatever you want
MASTER_PASSWORD = "letmein123"

root = tk.Tk()
root.title("Password Manager Login")
root.geometry("300x150")

label = tk.Label(root, text="Enter Master Password:")
label.pack(pady=10)

entry = tk.Entry(root, show="*", width=25)
entry.pack()
entry.focus()

login_btn = tk.Button(root, text="Login", command=verify_password)
login_btn.pack(pady=10)

root.mainloop()
