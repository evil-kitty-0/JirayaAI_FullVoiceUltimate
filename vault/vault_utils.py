from cryptography.fernet import Fernet
from config import VAULT_KEY
import os

fernet = Fernet(VAULT_KEY)

def encrypt_note(note_text, filename):
    encrypted = fernet.encrypt(note_text.encode())
    path = os.path.join("vault", filename + ".vault")
    with open(path, "wb") as f:
        f.write(encrypted)

def decrypt_note(filename):
    path = os.path.join("vault", filename + ".vault")
    with open(path, "rb") as f:
        encrypted = f.read()
    return fernet.decrypt(encrypted).decode()
