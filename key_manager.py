# key_manager.py
from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

def generate_key():
    """Generate a new encryption key and save it to a file."""
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key

def load_key():
    """Load the encryption key from a file."""
    if not os.path.exists(KEY_FILE):
        return generate_key()
    with open(KEY_FILE, "rb") as f:
        return f.read()
