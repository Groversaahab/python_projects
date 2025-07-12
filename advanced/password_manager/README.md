Introduction:
This is a python based password manager
It has a CLI(Command Line Interface) for taking user input
It uses a master password to make a key which is used to encrypt all the credentials that are stored in its vault
Multiple users may use this application on a single machine.

Installing instructions:
To run this application simple git clone this folder.
Add a folder/directory named data in password_manager, ie password_manager/data/
In data add 2 files named username_data.json and key.json.
Add an empty dictionary ({}, open and close curly brackets)
Now you need to convert password_manager (directory) to python venv.
Now you need to install the following libraries in this python venv.
1. argparse
2. sys
3. json
4. os
5. bcrypt
6. cryptography
7. base64
Now everything that needs to be installed is ready

To run we activate the pythin venv and run the application using the following syntax

python3 password_manager.py [flag] [input1] [input2] [input3]

these are the availabe flags, these may also be accessed using "-h" flag using the above syntax in your command prompt

-h, --help            show this help message and exit
  -nm, --newmaster new_username masterpassword
                        Generates a vault for the given username with the provided master password
  -vo, --vaultopen username masterpassword
                        Open the vault for the user using the master password
  -ad, --addpassword tag username password
                        Saves the username and password combo under a tag in the vault
  -dt, --deletetag tag  Deletes tag and the stored info with tag
  -sh, --showpassword tag
                        Shows username and password linked to the tag
  -da, --deleteall      delete all data stored in vault
  -sa, --showall        shows all data stored in vault
  -cv, --closevault     Closes the currently open vault
  -dv, --deletevault username masterpassword
                        Delete the given vault if password matches

Usage Instructions:
1. First we need to make a new user (master) with a strong password using -nm/--newmaster we add a new user to 