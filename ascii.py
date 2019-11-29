def text_to_binary(text: str) -> list:
    binary_text = []
    for index, char in enumerate(text):
        binary_text.append("{0:b}".format(ord(char)))
    return binary_text


class ASCIIList(list):
    def __str__(self):
        res = ""
        for el in self:
            res += el + " "
        return res


def encode_by_pairing(binary_text: list) -> ASCIIList:
    encoded = ASCIIList()
    for elem in binary_text:
        if str(elem).count("1") % 2 == 0:
            encoded.append("0" + elem)
        else:
            encoded.append("1" + elem)
    return encoded


def encode_by_unpaired(binary_text: list) -> ASCIIList:
    encoded = ASCIIList()
    for elem in binary_text:
        if str(elem).count("1") % 2 != 0:
            encoded.append("0" + elem)
        else:
            encoded.append("1" + elem)
    return encoded


def binary_to_hex(binary_text: list) -> list:
    hex_text = []
    for elem in binary_text:
        h = hex(int(elem, 2))
        hex_text.append(h[h.index("x") + 1:])
    return hex_text


def from_binary_to_text(txt: str) -> str:
    txt = txt.replace(" ", "")
    txt = txt.replace("\n", "")
    txt = txt.replace("\t", "")

    res = ""
    while len(txt) > 0:
        res += chr(int(txt[:8], 2))
        txt = txt[8:]
    return res


def from_ascii_to_binary(txt: str) -> str:
    txt = txt.replace(" ", "")
    txt = txt.replace("\n", "")
    txt = txt.replace("\t", "")

    res = ""
    while len(txt) > 0:
        res += "0" + txt[1:8]
        txt = txt[8:]
    return res


if __name__ == "__main__":
    res = text_to_binary("MYKYTA")
    print(res)
    print(encode_by_pairing(res))
    print(from_binary_to_text(from_ascii_to_binary(str(encode_by_pairing(res)))))
    print(binary_to_hex(encode_by_pairing(res)))
