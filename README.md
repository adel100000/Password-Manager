# Password Manager

A secure and user-friendly password manager built in Python with Tkinter.  
It helps you safely store, encrypt, and manage your passwords all in one place.

---

## Features

- Strong AES encryption using the `cryptography` library
- Master password login for extra security
- Add, view, search, and delete saved passwords
- Generate strong random passwords
- Import and export passwords in CSV format
- Light/Dark mode toggle for a modern look
- Packaged as a standalone executable with PyInstaller

---

## Project Structure

- gui_test.py - Main graphical user interface
- password_manager_functions.py - Encryption and data handling
- login_window.py - Master password login window
- .gitignore - Files and folders to exclude from version control
- README.md - This documentation file

---

## Installation

1. Clone the repository:
   git clone https://github.com/adel100000/Password-Manager.git

2. Install dependencies:
   pip install cryptography

3. Run the application:
   python gui_test.py

---

## Usage

- **Add Passwords**
  Save your credentials securely.

- **View or Search**
  Display or search your saved passwords.

- **Generate Passwords**
  Quickly create strong random passwords.

- **Export and Import**
  Backup or restore your passwords using CSV files.

- **Dark Mode**
  Switch between light and dark themes for comfort.

---

## Security Notes

- Your passwords are always encrypted locally on your device.
- Never share your secret.key or passwords.txt files.
- The master password is only stored in memory during your session.

---

## License

This project is open source and available under the MIT License.
