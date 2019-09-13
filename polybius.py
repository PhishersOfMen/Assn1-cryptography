POLYBIUS = [
    ["a", "f", "e", "d", "x"],
    ["h", "j", "o", "u", "s"],
    ["t", "v", "p", "y", "g"],
    ["c", "r", "l", "i", "n"],
    ["q", "k", "b", "m", "w"]
]

def polybiusToNum(letterStr):
    letterStr.replace(" ", "")
    nums = []
    for c in letterStr:
        for rowIndex, row in enumerate(POLYBIUS):
            try:
                colIndex = row.index(c)
                nums.extend([str(rowIndex + 1), str(colIndex + 1)])
                
            except ValueError:
                pass
    return "".join(nums)

def polybiusToStr(numStr):
    # print(numStr)
    chars = []
    for i in range(0, len(numStr), 2):
        row = int(numStr[i]) - 1
        col = int(numStr[i+1]) - 1
        chars.append(POLYBIUS[row][col])
    return "".join(chars)
