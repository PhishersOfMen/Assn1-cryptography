"""
    This function takes a single binary value and the key, then evaluates whether or not each value at a given index is equivalent. 
    1 if different
    0 if the same
    Returns that evaluated value
"""
def xor(binary, key):
    # Adds a buffer to the binary value
    # i.e. 101 => 000101
    temp = "000000"
    binary = temp + binary
    binary = binary[-6:]
    
    # element by element evaluation of the xor gate using the binary value and the key value
    rvalue = ''
    for i in range(len(key)):
        if key[i] == binary[i]:
            rvalue = f'{rvalue}0'
        else:
            rvalue = f'{rvalue}1'
    
    return rvalue

"""
    This function takes an array of integers, converts them to binary, applies the key to them using the xor function, converts the binary values back to decimal
    Returns an array of decimal values
"""
def oneTimePad(value, key):
    # Key to Binary - repeated value if number smaller than 32
    key = bin(key)
    key = key[2:]
    key = key*6
    key = key[:6]

    # Convert the given decimal values to binary
    binArray = []
    for el in value:
        temp = bin(int(el))
        temp = temp[2:]
        binArray.append(temp)

    # Applies the key to the binary values
    results = []
    for el in binArray:
        rvalue = xor(el, key)
        # converts the applied binary values back to decimal
        temp = str(int(rvalue,2))
        if len(temp) == 1:
            temp = f"0{temp}"
        results.append(temp)
        

    return "".join(results)