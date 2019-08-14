# -*- coding: utf-8 -*-


# Initial permutation matrix
PI = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Initial key permutation matrix
CP_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

# Shifted key permutation matrix to get Ki+1
CP_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

# Expanded matrix (48bits after expansion) XORed with Ki
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

# S-BOXES matrix
S_BOXES = [

    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
     ],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
     ],

    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
     ],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
     ],

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
     ],

    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
     ],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
     ],

    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
     ]
]

# Permutation matrix following each S-BOX substitution for each round
P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

# Final permutation matrix of data after the 16 rounds
PI_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

# Matrix determining the shift for each round of keys
ROUND_KEY_SHIFT = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

ENCRYPTION = 1
DECRYPTION = 0


def string_to_bit_array(text):
    """Convert the string into a list of bits."""
    array = list()
    for char in text:
        bin_val = bin_value(char, 8)  # Get value of char in one byte
        array.extend([int(x) for x in list(bin_val)])  # Add the bits to the list
    return array


def bit_array_to_string(array):
    """Transform bit array to string."""
    result_string = ''.join(
        [chr(int(i, 2)) for i in
            [''.join([str(x) for x in s_bytes])
                for s_bytes in split_into_n(array, 8)]]
    )
    return result_string


def bin_value(val, bit_size):
    """Return the binary value as a string of the given size."""
    bin_val = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(bin_val) > bit_size:
        raise "Binary value larger than expected!"
    while len(bin_val) < bit_size:
        bin_val = "0" + bin_val  # Add 0s to satisfy size
    return bin_val


def split_into_n(s, n):
    """Split into lists - each of size 'n'."""
    return [s[k:k + n] for k in range(0, len(s), n)]


class Des:
    def __init__(self):
        self.text = None
        self.passwd = None
        self.keys = list()

    def run(self, key, text, action=ENCRYPTION, padding=False):
        """Run the DES algorithm."""
        self.text = text
        self.passwd = key

        if padding and action == ENCRYPTION:
            self.add_padding()
        elif len(self.text) % 8 != 0:  # If not padding specified data size must be multiple of 8 bytes
            raise "Data size should be multiple of 8"

        self.generate_keys()  # Generate all the keys
        text_blocks = split_into_n(self.text, 8)  # Split the text in blocks of 8 bytes so 64 bits
        result = list()
        for block in text_blocks:  # Loop over all the blocks of data
            block = string_to_bit_array(block)  # Convert the block in bit array
            block = self.permutation(block, PI)  # Apply the initial permutation
            L, R = split_into_n(block, 32)  # L(LEFT), R(RIGHT)
            temp = None
            for i in range(16):  # Perform 16 rounds
                d_e = self.expansion(R, E)  # Expand R to 48 bits
                if action == ENCRYPTION:
                    temp = self.xor(self.keys[i], d_e)  # Use the Ki when encrypting
                else:
                    temp = self.xor(self.keys[15 - i], d_e)  # Use the last key when decrypting
                temp = self.substitute(temp)  # Apply the S-BOXES
                temp = self.permutation(temp, P)
                temp = self.xor(L, temp)
                L = R
                R = temp
            result += self.permutation(R + L, PI_1)  # Perform the last permutation & append the RIGHT to LEFT
        final_res = bit_array_to_string(result)
        if padding and action == DECRYPTION:
            return self.remove_padding(final_res)  # Remove the padding if decrypting and padding is used
        else:
            return final_res  # Return the final string of processed data

    def substitute(self, d_e):
        """Substitute bytes using S-BOXES."""
        sub_blocks = split_into_n(d_e, 6)  # Split bit array into sub_blocks of 6 bits each
        result = list()
        for i in range(len(sub_blocks)):  # For all the sub_blocks
            block = sub_blocks[i]
            row = int(str(block[0]) + str(block[5]), 2)  # Find row with the first & last bit
            column = int(''.join([str(x) for x in block[1:][:-1]]), 2)  # Column value based on 2nd, 3rd, 4th & 5th bit
            val = S_BOXES[i][row][column]  # Resulting value in the S-BOX for specific round
            bin = bin_value(val, 4)  # Convert decimal value to binary
            result += [int(x) for x in bin]  # Append the binary to the resulting list
        return result

    def permutation(self, block, table):
        """Perform permutation of the given block using the given table."""
        return [block[x - 1] for x in table]

    def expansion(self, block, table):
        """Perform expansion of d to mach the size of Ki (48 bits)."""
        return [block[x - 1] for x in table]

    def xor(self, t1, t2):
        """Perform XOR & return the list."""
        return [x ^ y for x, y in zip(t1, t2)]

    def generate_keys(self):
        """Generate all the keys."""
        self.keys = []
        key = string_to_bit_array(self.passwd)
        key = self.permutation(key, CP_1)  # Perform initial permutation on the key
        g, d = split_into_n(key, 28)  # Split into g (LEFT) & d (RIGHT)
        for i in range(16):  # Apply the 16 rounds
            g, d = self.shift(g, d, ROUND_KEY_SHIFT[i])  # Shift the key according to the round
            tmp = g + d  # Merge them
            self.keys.append(self.permutation(tmp, CP_2))  # Perform the permutation to get the Ki

    def shift(self, g, d, n):
        """Shift a list of the given value."""
        return g[n:] + g[:n], d[n:] + d[:n]

    def add_padding(self):
        """Add padding to the data according to PKCS5 specification."""
        pad_len = 8 - (len(self.text) % 8)
        self.text += pad_len * chr(pad_len)

    def remove_padding(self, data):
        """Remove the padding from the data."""
        pad_len = ord(data[-1])
        return data[:-pad_len]

    def encrypt(self, key, text, padding=True):
        """Perform encryption."""
        return self.run(key, text, ENCRYPTION, padding)

    def decrypt(self, key, text, padding=True):
        """Perform decryption."""
        return self.run(key, text, DECRYPTION, padding)


if __name__ == '__main__':
    # des_algorithm.py executed as script
    print("Nothing to execute!")
