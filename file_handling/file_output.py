# -*- coding: utf-8 -*-


def save_file(mode):
    """Decide whether the file should be saved."""
    if mode == "E":
        while True:
            s_file = input("Enter S to save encrypted text to file or N not to save:")
            if s_file == "S":
                return "S"
            elif s_file == "N":
                break
            else:
                print("Wrong input! Please try again.\n")
    elif mode == "D":
        while True:
            s_file = input("Enter S to save decrypted text to file or N not to save:")
            if s_file == "S":
                return "S"
            elif s_file == "N":
                break
            else:
                print("Wrong input! Please try again.\n")
    else:
        print("Wrong input! Please try again.\n")


def write_to_file(cont):
    """Write to file."""
    file_name = input("Enter the name of file you want to save:")
    with open("{}".format(file_name), "w") as user_file:
        user_file.write(cont)
        user_file.close()
        print("File successfully saved!\n")


if __name__ == '__main__':
    # file_output.py executed as script
    print("Nothing to execute!")
