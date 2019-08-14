# -*- coding: utf-8 -*-


def encrypt_decrypt():
    """Decide whether to encrypt or decrypt."""
    while True:
        choice = input("Enter E for encryption or D for decryption:")
        if choice == "E":
            return "E"
        elif choice == "D":
            return "D"
        else:
            print("Wrong input! Please try again.\n")


def text_input(mode):
    """Enter text to be encrypted or decrypted."""
    while True:
        text = input("Enter text:")
        if mode == "D" and len(text) < 8:
            print("Cannot decrypt less than 8 bytes!")
        else:
            return text


def show_output(mode, text):
    """Decide whether to show or not show output."""
    while True:
        show = input("Enter Y to show output else enter N.")
        if show == "Y" and mode == "E":
            print("Encrypted text:")
            print("'{}'".format(text))
            break
        elif show == "Y" and mode == "D":
            print("Decrypted text:")
            print("'{}'".format(text))
            break
        elif show == "N":
            break
        else:
            print("Wrong input! Please try again.\n")


if __name__ == '__main__':
    # user_io.py executed as script
    print("Nothing to execute!")
