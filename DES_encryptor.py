# -*- coding: utf-8 -*-

import user_and_key_io.user_io as u
import user_and_key_io.key_io as k
import file_handling.file_input as fi
import file_handling.file_output as fo
from des_algorithm import Des


def decor_aster(func):
    """Wrap text in asterisks."""
    def wrap():
        print("***************")
        func()
        print("***************")
    return wrap


def decor_dash(func):
    """Wrap text in dashes."""
    def wrap():
        print("--------------------------------------------------")
        func()
        print("--------------------------------------------------")
    return wrap


@decor_aster
def project_name():
    """Print project name."""
    print("DES Encryptor")


@decor_dash
def main_options():
    """Print main options for choice of algorithm to be used and exit."""
    print("\nD - DES algorithm")
    print("T - 3DES algorithm")
    print("EXIT - close the encryptor\n")


if __name__ == '__main__':
    # DES_encryptor.py executed as script

    run = True
    # Print wrapped project name
    project_name()

    while run:
        # Print main options and accept user choice
        main_options()
        main_choice = input("Enter your choice:")

        if main_choice == "D":
            # DES
            mode = u.encrypt_decrypt()  # Set mode to encryption or decryption
            l_file = fi.text_or_file()  # Load text from file or enter manually

            if l_file == "Y":
                m_text = fi.load_file(mode, l_file)
                m_key = k.key_input()
            else:
                m_text = u.text_input(mode)
                m_key = k.key_input()

            d = Des()

            if mode == "E":
                result_text = d.encrypt(m_key, m_text, True)
                u.show_output(mode, result_text)
                k.key_output(mode, m_key)
                save_file = fo.save_file(mode)
                if save_file == "S":
                    cont = result_text.encode("utf-8")
                    fo.write_to_file(str(cont))
                    print(cont)
            elif mode == "D":
                result_text = d.decrypt(m_key, m_text, True)
                u.show_output(mode, result_text)
                k.key_output(mode, m_key)
                if save_file == "S":
                    cont = result_text
                    fo.write_to_file(cont)
            else:
                print("Something went wrong... ¯\_(ツ)_/¯\n")

        elif main_choice == "T":
            #  3DES
            mode = u.encrypt_decrypt()  # Set mode to encryption or decryption
            l_file = fi.text_or_file()  # Load text from file or enter manually

            if l_file == "Y":
                m_text = fi.load_file(mode, l_file)
            else:
                m_text = u.text_input(mode)

            m_key_one = k.key_input()  # Enter the three independent 56 bit keys
            m_key_two = k.key_input()
            m_key_three = k.key_input()

            key_list = [m_key_one, m_key_two, m_key_three]  # Save the keys in list for easier manipulation
            for x in range(3):  # Run DES 3 times, each time with different key (3TDEA - strongest)

                d = Des()

                if mode == "E":
                    result_text = d.encrypt(key_list[x], m_text, True)
                    m_text = result_text
                else:
                    result_text = d.decrypt(key_list[x], m_text, True)
                    m_text = result_text

            u.show_output(mode, result_text)  # Show encrypted text
            save_file = fo.save_file(mode)
            if save_file == "S":
                cont = result_text
                fo.write_to_file(cont)
            k.keys_output(mode, m_key_one, m_key_two, m_key_three)

        elif main_choice == "EXIT":
            # Close the encryptor
            print("See you soon!")
            run = False
        else:
            print("Wrong input! Please try again.")
            print("------------------------------")
