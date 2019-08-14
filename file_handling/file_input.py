# -*- coding: utf-8 -*-


def text_or_file():
    """Load from file or input manually."""
    while True:
        load_choice = input("Enter X to enter text manually or F to load from file.")
        if load_choice == "F":
            return "Y"
        elif load_choice == "X":
            return "N"
        else:
            print("Wrong input! Please try again.\n")


def load_file(mode, l_file):
    """Decide which file should be loaded."""
    if l_file == "Y":
        while True:
            file_name = input("Enter the name of file you want to load:")
            user_file = open("{}".format(file_name), "r")
            if mode == "D":  # Reading bytes - converting to string /// not working - encrypted only ///
                utf_cont = user_file.read()
                cont = str(utf_cont)
            else:
                cont = user_file.read()
            user_file.close()
            if len(cont) < 8 and mode == "D":
                print("Cannot decrypt less than 8 bytes!")
            else:
                return cont
    elif l_file == "N":
        return "N"
    else:
        print("Wrong input! Please try again.\n")


if __name__ == '__main__':
    # file_input.py executed as script
    print("Nothing to execute!")
