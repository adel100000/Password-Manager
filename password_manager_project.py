from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"
DATA_FILE = "passwords.txt"


def load_or_create_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
        print("[✔] New encryption key created.\n")
    else:
        print("[✔] Encryption key loaded.\n")
    with open(KEY_FILE, "rb") as key_file:
        return Fernet(key_file.read())


def add_password(fernet):
    service = input("Enter the service name (e.g., Gmail): ")
    username = input("Enter the username/email: ")
    password = input("Enter the password: ")

    combined = f"{service} | {username} | {password}"
    encrypted = fernet.encrypt(combined.encode())

    with open(DATA_FILE, "ab") as f:
        f.write(encrypted + b"\n")

    print("[✔] Password saved.\n")


def view_passwords(fernet):
    if not os.path.exists(DATA_FILE):
        print("[!] No saved passwords.\n")
        return

    with open(DATA_FILE, "rb") as f:
        lines = f.readlines()
        if not lines:
            print("[!] No saved passwords.\n")
            return

        print("\n[Saved Passwords]:")
        for idx, line in enumerate(lines, start=1):
            decrypted = fernet.decrypt(line.strip()).decode()
            print(f"{idx}. {decrypted}")
        print()


def search_passwords(fernet):
    term = input("Enter service name to search: ").lower()

    if not os.path.exists(DATA_FILE):
        print("[!] No saved passwords.\n")
        return

    found = False
    with open(DATA_FILE, "rb") as f:
        lines = f.readlines()
        for line in lines:
            decrypted = fernet.decrypt(line.strip()).decode()
            if term in decrypted.lower():
                if not found:
                    print("\n[Matching Entries]:")
                print(" -", decrypted)
                found = True

    if not found:
        print("[!] No matches found.\n")
    else:
        print()


def edit_password(fernet):
    view_passwords(fernet)

    if not os.path.exists(DATA_FILE):
        return

    lines = []
    with open(DATA_FILE, "rb") as f:
        lines = f.readlines()

    if not lines:
        return

    try:
        idx = int(input("Enter the number of the entry to edit: "))
        if idx < 1 or idx > len(lines):
            print("[!] Invalid selection.\n")
            return
    except ValueError:
        print("[!] Invalid input.\n")
        return

    decrypted = fernet.decrypt(lines[idx - 1].strip()).decode()
    parts = decrypted.split(" | ")

    print("\n[Current Entry]:")
    print(f"Service: {parts[0]}")
    print(f"Username: {parts[1]}")
    print(f"Password: {parts[2]}")

    new_password = input("Enter the new password: ")
    updated = f"{parts[0]} | {parts[1]} | {new_password}"
    encrypted = fernet.encrypt(updated.encode())

    lines[idx - 1] = encrypted + b"\n"

    with open(DATA_FILE, "wb") as f:
        f.writelines(lines)

    print("[✔] Password updated.\n")


def wipe_passwords(master_pwd):
    confirm = input("Enter master password to confirm wipe: ")
    double_confirm = input("Are you absolutely sure? Type YES to proceed: ")

    if confirm == master_pwd and double_confirm.upper() == "YES":
        with open(DATA_FILE, "wb") as f:
            pass
        print("[✔] All passwords wiped.\n")
    else:
        print("[✖] Wipe canceled.\n")


def backup_key():
    if not os.path.exists(KEY_FILE):
        print("[!] No key file to backup.\n")
        return

    backup_path = input("Enter backup file name (e.g., backup.key): ")
    with open(KEY_FILE, "rb") as original, open(backup_path, "wb") as backup:
        backup.write(original.read())

    print(f"[✔] Encryption key backed up to {backup_path}\n")


def restore_key():
    restore_path = input("Enter backup file to restore from: ")

    if not os.path.exists(restore_path):
        print("[!] Backup file not found.\n")
        return

    with open(restore_path, "rb") as backup, open(KEY_FILE, "wb") as original:
        original.write(backup.read())

    print("[✔] Encryption key restored.\n")


def main():
    print("=== Encrypted Password Manager ===")

    fernet = load_or_create_key()
    master_pwd = input("Set or enter your master password: ")

    while True:
        print("\nChoose an option:")
        print("1. Add a new password")
        print("2. View saved passwords")
        print("3. Search passwords")
        print("4. Edit a password")
        print("5. Wipe all passwords")
        print("6. Backup encryption key")
        print("7. Restore encryption key")
        print("8. Exit")

        choice = input("> ")

        if choice == "1":
            add_password(fernet)
        elif choice == "2":
            view_passwords(fernet)
        elif choice == "3":
            search_passwords(fernet)
        elif choice == "4":
            edit_password(fernet)
        elif choice == "5":
            wipe_passwords(master_pwd)
        elif choice == "6":
            backup_key()
        elif choice == "7":
            restore_key()
        elif choice == "8":
            print("Goodbye. Stay safe out there.")
            break
        else:
            print("[!] Invalid option. Try again.\n")


if __name__ == "__main__":
    main()

