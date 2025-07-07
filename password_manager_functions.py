from cryptography.fernet import Fernet
import os

# Create or load encryption key
def load_or_create_key():
    if os.path.exists("secret.key"):
        with open("secret.key", "rb") as f:
            key = f.read()
    else:
        key = Fernet.generate_key()
        with open("secret.key", "wb") as f:
            f.write(key)
    return Fernet(key)

# Save a new password (encrypted)
def save_password(service, username, password, fernet):
    record = f"{service} | {username} | {password}"
    encrypted = fernet.encrypt(record.encode())
    with open("passwords.txt", "ab") as f:
        f.write(encrypted + b"\n")

# Load all passwords (decrypted)
def load_passwords(fernet):
    if not os.path.exists("passwords.txt"):
        return ""
    output = ""
    with open("passwords.txt", "rb") as f:
        lines = f.readlines()
        for line in lines:
            decrypted = fernet.decrypt(line.strip()).decode()
            output += decrypted + "\n"
    return output.strip()

# Clear all saved passwords
def clear_passwords():
    with open("passwords.txt", "wb") as f:
        pass  # Just empties the file
    
import csv

def export_passwords_to_csv(fernet, filename="passwords_backup.csv"):
    """Decrypts and exports passwords to a CSV file."""
    try:
        with open("passwords.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                return False  # Nothing to export

        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Service", "Username", "Password"])  # Header row

            for line in lines:
                decrypted = fernet.decrypt(line.strip().encode()).decode()
                parts = decrypted.split("|")
                if len(parts) == 3:
                    writer.writerow([part.strip() for part in parts])

        return True
    except FileNotFoundError:
        return False
import csv

def import_passwords_from_csv(file_path, fernet):
    try:
        with open(file_path, "r") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header
            for row in reader:
                if len(row) == 3:
                    service, username, password = row
                    save_password(service, username, password, fernet)
        return True
    except Exception as e:
        print(f"Import failed: {e}")
        return False
import string
import random

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

    
