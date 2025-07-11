import bcrypt
import json

def hash_master_password(password: str) -> bytes:
    password_bytes = password.encode("utf-8")
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed_password

def verify_master_password(username: str, password: str) -> bool:
    with open("./data/username_data.json", "r") as file:
        loaded_dict = json.load(file)
        stored_hash = loaded_dict[username]
    return bcrypt.checkpw(password.encode("utf-8"), stored_hash.encode())

def save_master_password(username: str, password: str):
    hashed_password = hash_master_password(password)
    with open("./data/username_data.json", "r+") as file:
        loaded_dict = json.load(file)
        loaded_dict[username] = hashed_password.decode()
        file.seek(0)                           # go back to top of file
        json.dump(loaded_dict, file, indent=4)      # overwrite with new data
        file.truncate()

def delete_user(username: str, password: str):
    if verify_master_password(username, password):
        with open("./data/username_data.json", "r+") as file:
            loaded_dict = json.load(file)
            del loaded_dict[username]
            file.seek(0)                           # go back to top of file
            json.dump(loaded_dict, file, indent=4)      # overwrite with new data
            file.truncate()
    else:
        print("Wrong master password!!!")