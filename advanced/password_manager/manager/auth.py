import bcrypt
import json

def hash_master_password(password: str) -> bytes:
    password_bytes = password.encode("utf-8")
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed_password

def verify_master_password(username: str, password: str) -> bool:
    with open("./manager/username_data.json", "r") as file:
        loaded_dict = json.load(file)
        stored_hash = loaded_dict[username]
        file.close()
    return bcrypt.checkpw(password.encode("utf-8"), stored_hash)

def save_master_password(username: str, password: str):
    hashed_password = hash_master_password(password)
    with open("./manager/username_data.json", "w+") as file:
        loaded_dict = json.load(file)
        loaded_dict[username] = hashed_password
        json.dumps(loaded_dict, indent=4)
        file.close()

def delete_user(username: str, password: str):
    if verify_master_password(username, password):
        with open("./manager/username_data.json", "w+") as file:
            loaded_dict = json.load(file)
            del loaded_dict[username]
            json.dumps(loaded_dict, indent=4)
            file.close()
    else:
        print("Wrong master password!!!")