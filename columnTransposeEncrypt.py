import textwrap


def columnTransposeEncrypt(text, key):
    text = text.replace(" ", "")
    key = key.replace(" ", "")
    rowList = textwrap.wrap(text, len(key))

    valueList = []
    for k in key:
        valueList.append({"key": k, "vals": []})
    for i in rowList:
        for j in range(len(i)):
            valueList[j]["vals"].append(i[j])

    valueList = sorted(valueList, key=lambda k: k["key"])
    ciphertext = ""
    for i in valueList:
        print(i)
        ciphertext += str("".join(i["vals"]))

    return ciphertext

