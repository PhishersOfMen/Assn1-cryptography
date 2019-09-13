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
        # print(polyKey)
        ciphertext = columnTransposeEncrypt(plaintext, polyKey)
        # print(ciphertext)
        polyNums = polybiusToNum(ciphertext)
        # print(polyNums)
        if len(polyNums) % 2 == 0:
            polyNums = [ polyNums[i:i+2] for i in range(0, len(polyNums), 2)]
        else:
            temp = polyNums[:-1]
            polyNums = [ polyNums[i:i+2] for i in range(0, len(polyNums)-1, 2)]
            polyNums.append(f'0{temp}')
        # print(polyNums)
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
        # print(results)
        ciphertext = polybiusToStr(results)
        # print(ciphertext)
        polyKey = polybiusToStr(key)
        # print(polyKey)
        message = columnTransposeDecrypt(ciphertext, polyKey)
        print(f'\nDecrypted message: {message}')