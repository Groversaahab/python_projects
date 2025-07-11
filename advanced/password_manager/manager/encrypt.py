from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import base64
import bcrypt
import json

def derive_key(username: str, password: str) -> bytes:
    salt = salt_generator(username)
    password_bytes = password.encode('utf-8')
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=10_000
    )
    key = kdf.derive(password_bytes)
    return base64.urlsafe_b64encode(key)

def salt_generator(username: str) -> bytes:
    username_bytes = username.encode("utf-8")
    hashed_username = bcrypt.hashpw(username_bytes, bcrypt.gensalt())
    return hashed_username

def incrypt_data(data: str, key: bytes) -> bytes:
    f = Fernet(key)
    incrypted_data = f.encrypt(data.encode())
    return incrypted_data

def decrypt_data(increpted_data: str, key: bytes) -> str:
    f = Fernet(key)
    decrypted_data = f.decrypt(increpted_data).decode()
    return decrypted_data

def save_key(key:bytes):
    with open("./manager/key.json", "w+") as file:
        loaded_list = json.load(file)
        loaded_list.append(key)
        json.dumps(loaded_list, indent=4)
        file.close()

def delete_key():
    with open("./manager/key.json", "w+") as file:
        loaded_list = json.load(file)
        loaded_list.pop()
        json.dumps(loaded_list, indent=4)
        file.close()
