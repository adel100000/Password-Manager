# Password Manager

A secure and user-friendly **Password Manager** built in **Python**, featuring both **GUI (Tkinter)** and **Command-Line (CLI)** interfaces.  
It safely stores, encrypts, and manages your passwords locally — no cloud storage, no tracking.



##  Features

-  **AES Encryption** with the `cryptography` library (Fernet)
-  **Master Password Login** for enhanced security
-  Add, View, Search, Edit, and Delete stored credentials
-  **Generate strong random passwords**
-  Import and Export passwords in CSV format
-  Local-only data encryption (nothing ever leaves your device)
-  **Light/Dark mode** toggle for comfort
-  Built with a modular structure and packaged using **PyInstaller**

---

##  Project Structure

| File | Description |

 `gui_test.py`  Main graphical interface built with Tkinter 
| `password_manager_functions.py` | Handles encryption, file management, CSV import/export, and password generation |
| `password_manager_project.py` | Command-line version (terminal-based) |
| `.gitignore` | Files excluded from version control |
| `README.md` | Project documentation |



##  Technical Highlights

- **Encryption System:**  
  Uses `cryptography.Fernet` for AES-based symmetric encryption.  
  Automatically generates a unique `secret.key` on first run and stores it locally.  

- **Password Storage:**  
  All passwords are saved in encrypted form in `passwords.txt`.  
  Decryption happens only in memory during runtime — nothing stays in plain text.

- **Key Management:**  
  Includes built-in functions to **backup** and **restore** encryption keys for recovery.

- **Dual Interface Design:**  
  Both GUI and CLI versions share the same encryption logic, showing modular code reuse.

- **Customization:**  
  GUI version supports a **Light/Dark theme system**, using color dictionaries for dynamic UI updates.



##  Installation

```bash
# Clone the repository
git clone https://github.com/adel100000/Password-Manager.git
cd Password-Manager

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required dependencies
pip install cryptography


To run the GUI version:

python gui_test.py


To run the Command-Line version:

python password_manager_project.py

## Usage

Add Passwords: Securely store new credentials
View/Search: Display or search saved passwords
Edit Passwords (CLI only): Update stored credentials
Generate Passwords: Create strong random passwords automatically
Export/Import: Backup or restore passwords with CSV files
Dark Mode: Switch between light and dark UI themes
Wipe Data: Permanently delete all stored passwords (with confirmation)

## Libraries Used

cryptography – AES encryption with Fernet

tkinter – GUI creation and event handling

csv – Import/export of password data

os – File management and key handling

string & random – Password generation

tkinter.messagebox, simpledialog, filedialog, scrolledtext – GUI utilities

## Security Notes

All passwords are encrypted locally on your device.

Never share your secret.key or passwords.txt files.

The master password is stored only in memory during runtime.

Always keep a backup of your key file (secret.key) in a safe place.

## License

This project is open-source and available under the MIT License.
