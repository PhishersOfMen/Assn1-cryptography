import sys

from Config import config
from columnTransposeDecrypt import columnTransposeDecrypt
from columnTransposeEncrypt import columnTransposeEncrypt
from oneTimePad import oneTimePad
from polybius import polybiusToStr, polybiusToNum

while True:
    # User Input
    encrypt, plaintext, key = config()
    otpKey = int(key[-2:])
    key = key[:-2]

    # Encryption Path
    if encrypt:
        polyKey = polybiusToStr(key)
        ciphertext = columnTransposeEncrypt(plaintext, polyKey)
        polyNums = polybiusToNum(ciphertext)
        results = oneTimePad(polyNums, otpKey)
        print(results)
    
    # Decryption Path
    else:
        results = oneTimePad(plaintext, otpKey)
        ciphertext = polybiusToStr(results)
        polyKey = polybiusToStr(key)
        message = columnTransposeDecrypt(ciphertext, polyKey)
        print(message)