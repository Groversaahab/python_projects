from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import base64
import bcrypt
import json

def create_vault(username: str):
    dic = {}
    with open(f"./data/{username}.json", "w") as file:
        json.dump(dic, file, indent=4)

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

def encrypt_data(data: str, key: bytes) -> bytes:
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data: str, key: bytes) -> str:
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data.encode()).decode()
    return decrypted_data

def save_key(username: str, key:bytes):
    with open("./data/key.json", "r+") as file:
        loaded_list = json.load(file)
        loaded_list.append(username)
        loaded_list.append(key.decode())
        file.seek(0)                           # go back to top of file
        json.dump(loaded_list, file, indent=4)      # overwrite with new data
        file.truncate()

def delete_key():
    with open("./data/key.json", "r+") as file:
        loaded_list = json.load(file)
        loaded_list = []
        file.seek(0)                           # go back to top of file
        json.dump(loaded_list, file, indent=4)      # overwrite with new data
        file.truncate()

def username_key_access() -> list:
    with open("./data/key.json", "r") as file:
        loaded_list = json.load(file)
        master_username = loaded_list[0]
        key = loaded_list[1].encode()
    return [master_username, key]

def vault_append(tag: str, username: str, password: str):
    [master_username, key] = username_key_access()
    encrypted_username = encrypt_data(username, key).decode()
    encrypted_password = encrypt_data(password, key).decode()
    encrypted_creds = [encrypted_username, encrypted_password]
    with open(f"./data/{master_username}.json", "r+") as file:
        loaded_dict = json.load(file)
        if tag in loaded_dict:
            print("please use another tag, this tag already exists!")
        else:
            loaded_dict[tag] = encrypted_creds
            file.seek(0)                           # go back to top of file
            json.dump(loaded_dict, file, indent=4)      # overwrite with new data
            file.truncate()
            print(f"Credentials with tag {tag} added!")

def vault_access(tag: str) -> list:
    [master_username, key] = username_key_access()
    with open(f"./data/{master_username}.json", "r") as file:
        loaded_dict = json.load(file)
        if tag not in loaded_dict:
            print(f"No credentials with tag {tag} in vault")
            return []
        encrypted_creds = loaded_dict[tag]
    decrypted_username = decrypt_data(encrypted_creds[0], key)
    decrypted_password = decrypt_data(encrypted_creds[1], key)
    decrypted_creds = [decrypted_username, decrypted_password]
    return decrypted_creds

def vault_del(tag:str):
    [master_username, key] = username_key_access()
    with open(f"./data/{master_username}.json", "r+") as file:
        loaded_dict = json.load(file)
        if tag in loaded_dict:
            del loaded_dict[tag]
            file.seek(0)
            json.dump(loaded_dict, file, indent=4)
            file.truncate()
            print(f"Credentials with tag {tag} deleted!!")
        else:
            print(f"No credentials with tag {tag} in vault")