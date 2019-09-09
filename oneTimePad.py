def xor(binary, key):
    key = bin(key)
    key = key[2:]
    # TODO: padding for binary
    # TODO: loop through key again if short
    rvalue = ''
    for i in range(len(key)):
        if key[i] == binary[i]:
            rvalue = f'{rvalue}0'
        else:
            rvalue = f'{rvalue}1'
    return rvalue

def oneTimePad(value, key):
    binArray = []
    for el in value:
        temp = bin(el)
        temp = temp[2:]
        binArray.append(temp)

    results = []
    for el in binArray:
        rvalue = xor(el, key)
        results.append(int(rvalue,2))

    return results