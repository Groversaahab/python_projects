Introduction: \
This is a python based password manager \
It has a CLI(Command Line Interface) for taking user input \
It uses a master password to make a key which is used to encrypt all the credentials that are stored in its vault \
Multiple users may use this application on a single machine. 

Installing instructions: \
To run this application simply git clone this folder. \
Add a folder/directory named data in password_manager, ie password_manager/data/ \
Now you need to convert password_manager (directory) to python venv. 

Now you need to install the following libraries in this python venv
1. argparse
2. sys
3. json
4. os
5. bcrypt
6. cryptography
7. base64

Now everything that needs to be installed is ready

Usage Instructions: \
To run we activate the pythin venv and run the application using the following syntax \
python3 password_manager.py [flag] [input1] [input2] [input3] \
These are the availabe flags, these may also be accessed using "-h" flag using the above syntax in your command prompt 

-h, --help            show this help message and exit \
  -nm, --newmaster new_username masterpassword \
                        Generates a vault for the given username with the provided master password \
  -vo, --vaultopen username masterpassword \
                        Open the vault for the user using the master password \
  -ad, --addpassword tag username password \
                        Saves the username and password combo under a tag in the vault \
  -dt, --deletetag tag  Deletes tag and the stored info with tag \
  -sh, --showpassword tag \
                        Shows username and password linked to the tag \
  -da, --deleteall      delete all data stored in vault \
  -sa, --showall        shows all data stored in vault \
  -cv, --closevault     Closes the currently open vault \
  -dv, --deletevault username masterpassword \
                        Delete the given vault if password matches 

Running order:
1.  First we need to make a new user (master) with a strong password using -nm/--newmaster we add a new user to our user database \
    This password must be strong because this will be used for encrypting the save credentials \
    This password must never be forgotten \
    This also makes a vault where the credentials will be saved (encrypted json file)
2.  Once a new user is made we need to open the vault to start saving our passwords in it. Use -vo or --vaultopen to open your vault
3.  Once vault is opened we can now add credentials with a unique tag (user decided) to our vault using -ad or --addpassword flags. \
    Tag should be unique and east to remember because it will be used to access your credentials later.
4.  To delete a credential use -dt or --deletetag with the tag of the credentials to delete. \
    This cannot be reversed, hence be careful.
5.  To access your credentials use -sh or --showpassword to get the credential linked to the tag provided.
6.  You may acccess all your data with -sa --showall
7.  Caution: Please use -ad, -dt, -sh, -da and -sa only with vault open otherwise it will throw error
8.  Once vault usage is finished, close to vault using -cv ar --closevault. \
    Make sure to close vault after using your password manager.
9.  Deleting user maybe done using -dv or --deletevault 

Hope your passwords stay safe in my password manager ;)