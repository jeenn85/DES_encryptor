# DES & 3DES Encryptor
Simple but pure Python DES & 3DES implementation written as a part of semestral thesis.
No cryptographic libraries - especially regarding DES or 3DES were used.

## Algorithm specification
DES & 3DES algorithm in ECB mode (Electronic Codebook) implemented according to specifics:
* [https://en.wikipedia.org/wiki/Data_Encryption_Standard](https://en.wikipedia.org/wiki/Data_Encryption_Standard),
* [https://en.wikipedia.org/wiki/DES_supplementary_material](https://en.wikipedia.org/wiki/DES_supplementary_material),
* [https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation),
* [https://en.wikipedia.org/wiki/Triple_DES](https://en.wikipedia.org/wiki/Triple_DES).
Padding used according to PKCS5 specification. 3DES uses 3 different keys.

### How to use it?
In application menu, you can decide whether to use DES ("D") or 3DES ("T").
Then you decide mode, that will be used E - encryption or D - decryption.
You can input the text from console or from a file.txt, then you will be prompted to provide the key(s) used for de/encryption.
Output can be shown, but it's not a condition, you can save the output to a file.txt.
Unfortunately saving and loading encrypted .txt files has not been fully resolved - due to non functioning decoding of bytes array. When saving the file, the variable holding the encrypted text is fine, but we can write it only in bytes array and not in utf-8 or ascii encoding.
When loading bytes array from a file, bytes array is correctly loaded, but python is unable to convert it to ascii or utf-8 string, because it thinks that we already have a string.
