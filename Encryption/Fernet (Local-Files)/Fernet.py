# Imports packages
import os
import dotenv
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()

KEY = os.getenv("KEY")
PASSWORD = os.getenv("PASSWORD")
KEY_BACKUP = os.getenv("KEY_BACKUP")


# Asks users for their password
def pass_check():

    user_input = input("Enter password: ")
    if user_input == PASSWORD:
        validity = True

        return(validity)
    
    else:
        print("Try again.")
        pass_check()

# Welcome function
def welcome():

    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Generate new key")
    print("4. Input key and use to encrypt / decrypt")
    print("5. Print out your current key")
    print("6. Set password (Advanced Users only!!!)")
    print("7. Reset Password and Key")
    print("8. Manage Keys")
    print("9. Store Text")

    choice = int(input("Input number: "))
    return choice

# Encrypt function
def encrypt_func():

    text = str(input("Input text: "))
    data = bytes(text, encoding="utf-8")
    cipher = Fernet(KEY)
    encrypted = cipher.encrypt(data)

    return(str(encrypted))

# Decrypt function
def decrypt_func():

    if pass_check() == True:

        data = str(input("Input encrypted text: "))
    
        cipher = Fernet(KEY)
        decrypted = cipher.decrypt(data)
        return(str(decrypted))
    else:
        pass_check()


# Key generation
def key_gen():

    if pass_check() == True:

        key = Fernet.generate_key()
        key_str = key.decode("utf-8", "strict")

        dotenv.set_key(".env", "KEY", key_str)
    else:
        pass_check()

# Import custom keys so you can share encrypted messages with others
def custom_key():

    if pass_check() == True:

        key = input("Input key: ")
        key = bytes(key, encoding="utf-8")
        key_str = key.decode("utf-8", "strict")
        dotenv.set_key(".env", "KEY", key_str)        
    else:
        pass_check()


    

# Prints out key, you can also read it directly from "thekey.key" file
def key_print():
    
    if pass_check() == True:
        print(KEY)
    else:
        pass_check()

# Changes password
def set_pass():
    
    print("Warning for security reasons this will reset your key as well so you cant access someone elses encryptions by resetting password.")
    key_gen()

    password = (input("Input new Password: "))
    print("The script will now exit and you password will be affective on next launch")

    dotenv.set_key(".env", "PASSWORD", password)
    exit()

    

# Resets the password and generates a new key
def reset():

    key_gen()
    default = "Alpine"
    
    dotenv.set_key(".env", "PASSWORD", default)

def managekeys():

    print("1. Backup a key")
    print("2. Delete backed up key")
    print("3. Restore key from backed up key")
    print("0. Go back to main menu")
    option_key = int(input("Input a number: "))

    match option_key:

        case 1:
            if KEY_BACKUP != '':

                backedupkey = input("Input the key: ")
                dotenv.set_key(".env", "KEY_BACKUP", backedupkey)
            else:
                print("Delete this backed up key first")
                managekeys()
        case 2:
            ask = input("Are you sure [y/n]]")

            if ask == "y":
                dotenv.set_key(".env", "KEY_BACKUP", '')
            else:
                welcome()
        case 3:
            ask = input("Are you sure [y/n]")

            if ask == "y":
                dotenv.set_key(".env", "KEY", KEY_BACKUP)
            else:
                welcome()
        case 0:
            welcome()

def storeencryptions():

    encrypted_text = input("Input the encrypted text you want to save: ")
    key_to_encrypt = input("Input the key used to encrypt the text: ")

    cipher = Fernet(key_to_encrypt)

    decrypted_text = str(cipher.decrypt(encrypted_text))
    if ENCRYPTED1 and DECRYPTED1 and ENCRYPTION_KEY1 == '':
        dotenv.set_key(".env", "ENCRYPTED1", encrypted_text)
        dotenv.set_key(".env", "DECRYPTED1", decrypted_text)
        dotenv.set_key(".env", "ENCRYPTION_KEY1", key_to_encrypt)
    elif ENCRYPTED2 and DECRYPTED1 and ENCRYPTION_KEY2 == '':
        dotenv.set_key(".env", "ENCRYPTED2", encrypted_text)
        dotenv.set_key(".env", "DECRYPTED2", decrypted_text)
        dotenv.set_key(".env", "ENCRYPTION_KEY2", key_to_encrypt)
    else:
        dotenv.set_key(".env", "ENCRYPTED3", encrypted_text)
        dotenv.set_key(".env", "DECRYPTED3", decrypted_text)
        dotenv.set_key(".env", "ENCRYPTION_KEY3", key_to_encrypt)

# Prompts user if they would like to end the script 
def end():

    end = input("End [y/n]")
    if end == "yes" or end == "y":
        exit()

if KEY == '':
    print("Either this is your first time running the script or YOU changed your key to '',no worries we are generating a new key for you.")
    print("Default password is Alpine you should change it after")
    key_gen()

# Controls the users choice throughout the script      
while True:

    #.env stuff
    load_dotenv()

    KEY = os.getenv("KEY")
    PASSWORD = os.getenv("PASSWORD")
    KEY_BACKUP = os.getenv("KEY_BACKUP")
    ENCRYPTED1 = os.getenv("ENCRYPTED1")
    ENCRYPTED2 = os.getenv("ENCRYPTED2")   
    ENCRYPTED3 = os.getenv("ENCRYPTED3")
    ENCRYPTION_KEY1= os.getenv("ENCRYPTION_KEY1")
    ENCRYPTION_KEY2= os.getenv("ENCRYPTION_KEY2")
    ENCRYPTION_KEY3= os.getenv("ENCRYPTION_KEY3")
    DECRYPTED1 = os.getenv("DECRYPTED1")
    DECRYPTED2 = os.getenv("DECRYPTED2")
    DECRYPTED3 = os.getenv("DECRYPTED3")

    choice = welcome()
    
    match choice:

        case 1:
            encrypt = encrypt_func()
            print(encrypt)
        case 2:
            decrypt = decrypt_func()
            print(decrypt)
        case 3:
            key_gen()
        case 4:
            custom_key()
        case 5:
            key_print()
        case 6:
            set_pass()
        case 7:
            reset()
        case 8:
            managekeys()
        case 9:
            storeencryptions()

    end()