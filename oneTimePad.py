def xor(binary, key):
    rvalue = "10101010"
    return rvalue

def oneTimePad(value, key):
    binary = bin(value)
    binary = binary[2:]

    rvalue = xor(binary, key)

    results = int(rvalue, 2)

    return results