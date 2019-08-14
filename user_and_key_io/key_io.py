# -*- coding: utf-8 -*-


def key_input():
    """
    Enter key to be used.
    Don't accept key shorter than 8 bytes.
    If key is longer than 8 bytes, cut it to 8 bytes.
    """
    while True:
        key = input("Enter 8 byte key:")
        if len(key) < 8:
            print("Key should be 8 bytes long!")
        elif len(key) > 8:
            key = key[:8]  # If entered key is too long, cut to 8 bytes
            print("Entered key cut to 8 bytes: '{}' was used as a key.".format(key))
            return key
        else:
            return key


def key_output(mode, used_key):
    """
    Return the key used for encryption or decryption,
    based on mode that was used.
    """
    if mode == "E":
        return print("Key used for encryption was: '{}'.".format(used_key))
    else:
        return print("Key used for decryption was: '{}'.".format(used_key))


def keys_output(mode, used_key_one, used_key_two, used_key_three):
    """
    Return the keys used for encryption or decryption,
    based on mode that was used.
    """
    if mode == "E":
        return print("Keys used for encryption were: '{}', '{}', '{}'.".format(
            used_key_one, used_key_two, used_key_three)
        )
    else:
        return print("Keys used for decryption were: '{}', '{}', '{}'.".format(
            used_key_one, used_key_two, used_key_three)
        )


if __name__ == '__main__':
    # key_io.py executed as script
    print("Nothing to execute!")