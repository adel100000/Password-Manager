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

## 🧩 Project Structure

| File | Description |
|------|--------------|
| `gui_test.py` | Main graphical interface built with Tkinter |
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
