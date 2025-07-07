import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext, filedialog
import password_manager_functions as pmf

# Define themes
LIGHT_THEME = {
    "bg": "#f7f9fb",
    "fg": "#222",
    "accent": "#1976d2",
    "text_bg": "#ffffff"
}

DARK_THEME = {
    "bg": "#212121",
    "fg": "#f0f0f0",
    "accent": "#64b5f6",
    "text_bg": "#2c2c2c"
}

current_theme = LIGHT_THEME

# Fonts
font_header = ("Segoe UI", 17, "bold")
font_normal = ("Segoe UI", 11)

# Load encryption key
fernet = pmf.load_or_create_key()

# Main window
root = tk.Tk()
root.title("Password Manager")
root.geometry("620x540")
root.resizable(False, False)

# Center window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (620/2))
y_cordinate = int((screen_height/2) - (540/2))
root.geometry(f"620x540+{x_cordinate}+{y_cordinate}")

root.configure(bg=current_theme["bg"])

# Header
header_label = tk.Label(root, text="Password Manager", font=font_header, bg=current_theme["bg"], fg=current_theme["fg"])
header_label.pack(pady=(15, 5))

# Text area
text_area = scrolledtext.ScrolledText(root, width=70, height=18, font=font_normal, wrap=tk.WORD)
text_area.pack(padx=10, pady=(0, 10))
text_area.tag_config("highlight", background="#ffff99")

# Functions
def add_password():
    service = simpledialog.askstring("Service", "Enter service name:")
    if not service:
        return
    username = simpledialog.askstring("Username", "Enter username/email:")
    if not username:
        return
    password = simpledialog.askstring("Password", "Enter password:")
    if not password:
        return
    pmf.save_password(service, username, password, fernet)
    status_var.set("Password saved successfully.")
    view_passwords()

def view_passwords():
    passwords = pmf.load_passwords(fernet)
    text_area.delete(1.0, tk.END)
    if passwords:
        text_area.insert(tk.END, "Saved Passwords:\n\n")
        text_area.insert(tk.END, passwords)
    else:
        text_area.insert(tk.END, "No passwords stored yet.")

def search_passwords():
    keyword = simpledialog.askstring("Search", "Enter service or username to search for:")
    if not keyword:
        return
    passwords = pmf.load_passwords(fernet)
    text_area.delete(1.0, tk.END)
    if passwords:
        matches = [line for line in passwords.split("\n") if keyword.lower() in line.lower()]
        if matches:
            text_area.insert(tk.END, "Search Results:\n\n")
            for line in matches:
                start = text_area.index(tk.END)
                text_area.insert(tk.END, line + "\n")
                end = text_area.index(tk.END)
                text_area.tag_add("highlight", start, end)
            status_var.set(f"Found {len(matches)} match(es).")
        else:
            text_area.insert(tk.END, "No matches found.")
            status_var.set("No matches found.")
    else:
        text_area.insert(tk.END, "No passwords stored yet.")
        status_var.set("No passwords stored.")

def copy_selected():
    try:
        selected_text = text_area.get(tk.SEL_FIRST, tk.SEL_LAST)
        root.clipboard_clear()
        root.clipboard_append(selected_text)
        messagebox.showinfo("Copied", "Selected text copied to clipboard.")
    except tk.TclError:
        messagebox.showwarning("No Selection", "Please select text to copy.")

def wipe_passwords():
    if messagebox.askyesno("Confirm Wipe", "Delete ALL passwords? This cannot be undone."):
        pmf.clear_passwords()
        text_area.delete(1.0, tk.END)
        status_var.set("All passwords wiped.")

def export_passwords():
    success = pmf.export_passwords_to_csv(fernet)
    if success:
        messagebox.showinfo("Export Complete", "Passwords exported to passwords_backup.csv.")
    else:
        messagebox.showwarning("Export Failed", "No passwords to export.")

def import_csv():
    file_path = filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*"))
    )
    if not file_path:
        return
    success = pmf.import_passwords_from_csv(file_path, fernet)
    if success:
        messagebox.showinfo("Success", "Passwords imported successfully.")
        view_passwords()
    else:
        messagebox.showerror("Error", "Failed to import passwords.")

def generate_password_gui():
    length = simpledialog.askinteger("Password Length", "Enter desired password length:", minvalue=6, maxvalue=64)
    if not length:
        return
    password = pmf.generate_password(length)
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Generated", f"Password generated and copied to clipboard.")

def toggle_theme():
    global current_theme
    current_theme = DARK_THEME if current_theme == LIGHT_THEME else LIGHT_THEME
    apply_theme()
    status_var.set("Theme toggled.")

def apply_theme():
    root.configure(bg=current_theme["bg"])
    header_label.config(bg=current_theme["bg"], fg=current_theme["fg"])
    text_area.config(bg=current_theme["text_bg"], fg=current_theme["fg"], insertbackground=current_theme["fg"])
    button_frame.config(bg=current_theme["bg"])
    status_bar.config(bg=current_theme["bg"], fg=current_theme["fg"])
    for widget in button_frame.winfo_children():
        widget.config(bg=current_theme["accent"], fg="white", activebackground=current_theme["accent"])

def exit_app():
    if messagebox.askokcancel("Exit", "Exit the application?"):
        root.destroy()

# Buttons Frame
button_frame = tk.Frame(root, bg=current_theme["bg"])
button_frame.pack(pady=10)

# Status bar
status_var = tk.StringVar()
status_var.set("Ready")
status_bar = tk.Label(root, textvariable=status_var, bd=1, relief=tk.SUNKEN, anchor="w",
                      bg=current_theme["bg"], fg=current_theme["fg"], font=("Segoe UI", 10))
status_bar.pack(fill=tk.X, side=tk.BOTTOM, ipady=2)

# Button styling
button_opts = dict(width=16, font=font_normal, pady=4)

# Buttons
buttons = [
    ("Add Password", add_password),
    ("View Passwords", view_passwords),
    ("Search Passwords", search_passwords),
    ("Copy Selection", copy_selected),
    ("Generate Password", generate_password_gui),
    ("Export to CSV", export_passwords),
    ("Import CSV", import_csv),
    ("Wipe All Passwords", wipe_passwords),
    ("Toggle Dark Mode", toggle_theme),
    ("Exit", exit_app)
]

for idx, (label, cmd) in enumerate(buttons):
    tk.Button(button_frame, text=label, command=cmd, bg=current_theme["accent"],
              fg="white", activebackground=current_theme["accent"], **button_opts).grid(row=idx // 2, column=idx % 2, padx=6, pady=6)

apply_theme()
root.mainloop()



