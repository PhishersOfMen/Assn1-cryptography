import sys

from Config import config
from columnTransposeDecrypt import columnTransposeDecrypt
from columnTransposeEncrypt import columnTransposeEncrypt
from oneTimePad import oneTimePad
from polybius import polybiusToStr, polybiusToNum

while True:
    # User Input
    encrypt, plaintext, key, showSteps = config()
    otpKey = int(key[-2:])
    key = key[:-2]

    # Encryption Path
    if encrypt:
        polyKey = polybiusToStr(key)
        if(showSteps):
            print(f"\nKey from Polybius square: {polyKey}")
        ciphertext = columnTransposeEncrypt(plaintext, polyKey)
        if(showSteps):
            print(f"Cipher text from columnar transposition: {ciphertext}")
        polyNums = polybiusToNum(ciphertext)
        if(showSteps):
            print(f"Polybius encrypted cipher text: {polyNums}")
        if len(polyNums) % 2 == 0:
            polyNums = [ polyNums[i:i+2] for i in range(0, len(polyNums), 2)]
        else:
            temp = polyNums[:-1]
            polyNums = [ polyNums[i:i+2] for i in range(0, len(polyNums)-1, 2)]
            polyNums.append(f'0{temp}')
        results = oneTimePad(polyNums, otpKey)
        print(f'\nEncrypted Message: {results}')
    
    # Decryption Path
    else:
        if len(plaintext) % 2 == 0:
            plaintext = [ plaintext[i:i+2] for i in range(0, len(plaintext), 2)]
        else:
            temp = plaintext[:-1]
            plaintext = [ plaintext[i:i+2] for i in range(0, len(plaintext)-1, 2)]
            plaintext.append(f'0{temp}')
        results = oneTimePad(plaintext, otpKey)
        if(showSteps):
            print(f"\nDecrypted text from one time pad: {results}")
        ciphertext = polybiusToStr(results)
        if(showSteps):
            print(f"Decrypted text from Polybius square: {ciphertext}")
        polyKey = polybiusToStr(key)
        if(showSteps):
            print(f"Key from Polybius square: {polyKey}")
        message = columnTransposeDecrypt(ciphertext, polyKey)
        print(f'\nDecrypted message: {message}')