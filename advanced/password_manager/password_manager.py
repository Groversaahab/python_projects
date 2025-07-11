import argparse
import sys
from manager import auth

# -----paths for the used files------

sys.path.append("./manager/")

# -----functions for application of calls-------
# -----making new user--------       Done

def new_master(args):
    username = args.read[0]
    master_password = args.read[1]
    auth.save_master_password(username, master_password)

# -----Opening Vault using master password--------         Passwored authentication --done
#                                                          Opening vault            --tobedone

def vault_open(args):
    username = args.read[0]
    master_password = args.read[1]
    if auth.verify_master_password(username, master_password):
        # Code
        filler = 1
    else:
        print("wrong master password!!!")

def add_password(args):
    tag = args.read[0]
    username = args.read[1]
    password = args.read[2]

def edit_tag(args):
    tag = args.read[0]
    username = args.read[1]
    password = args.read[2]

def delete_tag(args):
    tag = args.read[0]

def show_password(args):
    tag = args.read[0]

def delete_all():
    delete = 1

def show_all():
    show = 1

def close_vault():
    close = 1

# -----Deleting vault using master password--------      Deleting username and password from file --done
#                                                        Deleting vault                           --tobedone

def delete_vault(args):
    username = args.read[0]
    master_password = args.read[1]
    auth.delete_user(username, master_password)

# -----Description for the CLI(command line interface)-------

parser = argparse.ArgumentParser(description="A password manager built using python")

# -----Commands for commandline------

parser.add_argument("-nm", "--newmaster", type=str, nargs=2, metavar=("new_username","masterpassword"), default=None, help="Generates a vault for the given username with the provided master password")
parser.add_argument("-vo", "--vaultopen", type=str, nargs=2, metavar=("username", "masterpassword"), default=None, help="Open the vault for the user using the master password")
parser.add_argument("-ad", "--addpassword", type=str, nargs=3, metavar=("tag", "username", "password"), default=None, help="Saves the username and password combo under a tag in the vault")
parser.add_argument("-ed", "--edittag", type=str, nargs=3, metavar=("tag", "new/old_username", "newpassword"), default=None, help="Changes the username and password for the given tag")
parser.add_argument("-dt", "--deletetag", type=str, nargs=1, metavar="tag", default=None, help="Deletes tag and the stored info with tag")
parser.add_argument("-sh", "--showpassword", type=str, nargs=1, metavar="tag", default=None, help="Shows username and password linked to the tag")
parser.add_argument("-da", "--deleteall", help="delete all data stored in vault")
parser.add_argument("-sa", "--showall", help="shows all data stored in vault")
parser.add_argument("-cv", "--closevault", help="Closes the currently open vault")
parser.add_argument("-dv", "--deletevault", type=str, nargs=2, metavar=("username", "masterpassword"), default="", help="Delete the given vault if password matches")

# -----?????-----

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
elif args.deleteall != None:
    delete_all()
elif args.showall != None:
    show_all()
elif args.closevault != None:
    close_vault()
elif args.deletevault != None:
    delete_vault(args)