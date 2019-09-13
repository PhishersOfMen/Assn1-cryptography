 #goes throughout key and assigns a number for each letter.
def keyPosition(key):
    position = [] 
    for index, i in enumerate(key):
        previousLetters = key[:index]
        temp = 1
        for indexMinusOne, h in enumerate(previousLetters):
            if h > i:
                position[indexMinusOne] += 1
            else:
                temp += 1
        position.append(temp)
    return position

#goes throug empty matrix and fils with letters that have been sorted with the key position function.
def createDycrypter(keyPos, text):
    row = len(keyPos)
    col = int(len(text) / row)
    if col * row < len(text):
        col += 1
    emptyMat = []
    totalAdded = 0
    for f in range(col):
        emptyMat.append([])
        for k in range(row):
            if totalAdded < len(text):
               emptyMat[f].append('')
               totalAdded += 1          
    decrypter = emptyMat
    index = 0
    for num in range(len(keyPos)):
        i = keyPos.index(num+1)
        j = 0
        while (j < len(decrypter)) and (len(decrypter[j]) > i):
            decrypter[j][i] = text[index]
            j += 1
            index += 1
    return decrypter

 #my decrypted method   
def columnTransposeDecrypt(text, key):
    message = ""
    decrypter = createDycrypter(keyPosition(key), text)
    for j in range(len(decrypter)):
        for k in range(len(decrypter[j])):
            message += decrypter[j][k]
    return message
