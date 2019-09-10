import math

def columnTransposeDecrypt(text,key):
    decryptedMessage = ""
    #key values 
    keyIndex = 0
    keyList = sorted(list(key)) 
    #text values
    textIndex = 0
    textLength = float(len(text)) 
    textList = list(text)
    #get my col and row
    col = len(key) 
    row = int(math.ceil(textLength / col))  
    #get an empty matrix
    decrypt = [] 
    for _ in range(row): 
        decrypt += [[None] * col] 
    #fill empty matrix 
    for _ in range(col): 
        i = key.index(keyList[keyIndex]) 
  
        for j in range(row): 
            decrypt[j][i] = textList[textIndex] 
            textIndex += 1
        keyIndex += 1
    #decrypt my message.    
    decryptedMessage = ''.join(sum(decrypt, []))
    return decryptedMessage 