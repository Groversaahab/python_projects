import argparse

# -----functions for application of calls-------

def new_master(args):
    username = args.read[0]
    master_password = args.read[1]


# -----Description for the CLI(command line interface)-------

parser = argparse.ArgumentParser(description="A password manager built using python")

# -----Commands for commandline------

parser.add_argument("-nm", "--newmaster", type=str, nargs=2, metavar=("new_username","master_password"), default=None, help="Generates a vault for the given username with the provided master password")
parser.add_argument("-vo", "--vaultopen", type=str, nargs=2, metavar=("username", "master_password"), default=None, help="Open the vault for the user using the master password")
parser.add_argument("-ad", "--addpassword", type="str", nargs=3, metavar=("tag_for_usermame&password", "username", "password"), default=None, help="Saves the username and password combo under a tag in the vault")
parser.add_argument("-ed", "--edittag", type=str, nargs=3, metavar=("tag", "new/old username", "new password"), default=None, help="Changes the username and password for the given tag")
parser.add_argument("-dt", "--deletetag", type=str, nargs=1, metavar="tag", default=None, help="Deletes tag and the stored info with tag")
parser.add_argument("-sh", "--showpassword", type=str, nargs=1, metavar="tag", default=None, help="Shows username and password linked to the tag")
parser.add_argument("-da", "--deleteall", nargs=0, help="delete all data stored in vault")
parser.add_argument("-sa", "--showall", nargs=0, help="shows all data stored in vault")
parser.add_argument("-cv", "--closevault", nargs=0, help="Closes the currently open vault")
parser.add_argument("-dv", "--deletevault", type=str, nargs=2, metavar=("username", "masterpassword"), default="", help="Delete the given vault if password matches")

# ----?????-----

args = parser.parse_args()