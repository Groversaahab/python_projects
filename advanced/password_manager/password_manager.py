import argparse
import sys
from manager import auth
from manager import encrypt
import json
import os

# -----paths for the used files------

sys.path.append("./manager/")

# -----functions for application of calls-------
# -----making new user--------       Done

def new_master(args):
    username = args.newmaster[0]
    master_password = args.newmaster[1]
    auth.save_master_password(username, master_password)
    encrypt.create_vault(username)
    print("New user added!!")

# -----Opening Vault using master password--------         Passwored authentication --done
#                                                          Opening vault            --tobedone

# Add functionality for if vault already open
# Add functionality for checking if user exists

def vault_open(args):
    username = args.vaultopen[0]
    master_password = args.vaultopen[1]
    if auth.verify_master_password(username, master_password):
        key = encrypt.derive_key(username, master_password)
        encrypt.save_key(username, key)
        print("Vault opened!!")
    else:
        print("wrong master password!!!")

def add_password(args):
    tag = args.addpassword[0]
    username = args.addpassword[1]
    password = args.addpassword[2]
    encrypt.vault_append(tag, username, password)

def edit_tag(args):
    tag = args.edittag[0]
    username = args.edittag[1]
    password = args.edittag[2]
    encrypt.vault_append(tag, username, password)

def delete_tag(args):
    tag = args.deletetag[0]
    encrypt.vault_del(tag)

def show_password(args):
    tag = args.showpassword[0]
    print(encrypt.vault_access(tag))

def delete_all():
    [master_username, key] = encrypt.username_key_access()
    with open(f"./data/{master_username}.json", "r+") as file:
        loaded_dict = json.load(file)
        loaded_dict = {}
        file.seek(0)
        json.dump(loaded_dict, file, indent=4)
        file.truncate()

def show_all():
    [master_username, key] = encrypt.username_key_access()
    with open(f"./data/{master_username}.json", "r") as file:
        loaded_dict = json.load(file)
        for i in loaded_dict:
            encrypted_creds = loaded_dict[i]
            decrypted_creds = [encrypt.decrypt_data(encrypted_creds[0], key), encrypt.decrypt_data(encrypted_creds[1], key)]
            print(decrypted_creds)

# Add functionality for checking if vault already closed

def close_vault():
    encrypt.delete_key()
    print("Vault closed!!")

# -----Deleting vault using master password--------      Deleting username and password from file --done
#                                                        Deleting vault                           --tobedone

# Add functionality to check if user exists

def delete_vault(args):
    username = args.deletevault[0]
    master_password = args.deletevault[1]
    if auth.verify_master_password(username,master_password):
        auth.delete_user(username, master_password)
        os.remove(f"./data/{username}.json")
        print("User deleted!!")
    else:
        print("Wrong master password")

# -----Description for the CLI(command line interface)-------

parser = argparse.ArgumentParser(description="A password manager built using python")
# subparsers = parser.add_subparsers(dest="command", required=True)

# -----Commands for CLI------

parser.add_argument("-nm", "--newmaster", type=str, nargs=2, metavar=("new_username","masterpassword"), default=None, help="Generates a vault for the given username with the provided master password")
parser.add_argument("-vo", "--vaultopen", type=str, nargs=2, metavar=("username", "masterpassword"), default=None, help="Open the vault for the user using the master password")
parser.add_argument("-ad", "--addpassword", type=str, nargs=3, metavar=("tag", "username", "password"), default=None, help="Saves the username and password combo under a tag in the vault")
parser.add_argument("-ed", "--edittag", type=str, nargs=3, metavar=("tag", "new/old_username", "newpassword"), default=None, help="Changes the username and password for the given tag")
parser.add_argument("-dt", "--deletetag", type=str, nargs=1, metavar="tag", default=None, help="Deletes tag and the stored info with tag")
parser.add_argument("-sh", "--showpassword", type=str, nargs=1, metavar="tag", default=None, help="Shows username and password linked to the tag")

# added code

# subparsers.add_parser("closevault", help="Closes the currently open vault")
# subparsers.add_parser("cv", help="alias for closevault")
# subparsers.add_parser("deleteall", help="Deletes all data stored in the vault")
# subparsers.add_parser("da", help="alias for deleteall")
# subparsers.add_parser("showall", help="displays all data stored in the vault")
# subparsers.add_parser("sa", help="alias for showall")
# subparsers.add_parser("none", help="for using flags")

parser.add_argument("-da", "--deleteall", action="store_true", help="delete all data stored in vault")
parser.add_argument("-sa", "--showall", action="store_true", help="shows all data stored in vault")
parser.add_argument("-cv", "--closevault",action="store_true" , help="Closes the currently open vault")

parser.add_argument("-dv", "--deletevault", type=str, nargs=2, metavar=("username", "masterpassword"), default="", help="Delete the given vault if password matches")

# -----Parse the input given by user(tells python to look for inputs)-----

args = parser.parse_args()

if args.newmaster != None:
    new_master(args)
elif args.vaultopen != None:
    vault_open(args)
elif args.addpassword != None:
    add_password(args)
elif args.edittag != None:
    edit_tag(args)
elif args.deletetag != None:
    delete_tag(args)
elif args.showpassword != None:
    show_password(args)
elif args.deleteall:
    delete_all()
elif args.showall:
    show_all()
elif args.closevault:
    close_vault()
elif args.deletevault != None:
    delete_vault(args)