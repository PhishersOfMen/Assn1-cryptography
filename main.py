import sys

from Config import config
from columnTransposeDecrypt import columnTransposeDecrypt
from columnTransposeEncrypt import columnTransposeEncrypt
from oneTimePad import oneTimePad
from polybius import polybiusToStr, polybiusToNum

while True:
    # User Input
    encrypt, plaintext, key = config()
    otpKey = key[-2:]
    key = key[:-2]

    # Encryption Path
    if encrypt:
        polyKey = polybiusToStr(key)
        ciphertext = columnTransposeEncrypt(plaintext, polyKey)
        polyNums = polybiusToNum(ciphertext)
        results = oneTimePad(polyNums, otpKey)
        # TODO: merge results
        print(results)
    
    # Decryption Path
    else:
        results = oneTimePad(plaintext, otpKey)
        # TODO: merge results
        polyKey = polybiusToStr(results)
        message = columnTransposeDecrypt(polyKey, key) # TODO Check
        print(message)