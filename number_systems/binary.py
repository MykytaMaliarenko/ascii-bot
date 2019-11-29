import re

BINARY_REGEX = r"^[0-1\s\n]+$"


class MyBinary(list):
    """list of unicodes"""
    data: list

    def __init__(self, text: str = "", binary_text: str = "", ascii_text: str = ""):
        super().__init__()
        self.data = []

        if text:
            for char in text:
                self.data.append(ord(char))
        elif binary_text:
            binary_text = binary_text.replace(" ", "")
            while len(binary_text) > 0:
                self.data.append(int(binary_text[:7], 2))
                binary_text = binary_text[7:]
        elif ascii_text:
            ascii_text = ascii_text.replace(" ", "")
            while len(ascii_text) > 0:
                self.data.append(int(ascii_text[:8], 2))
                ascii_text = ascii_text[8:]

    def to_int(self) -> list:
        return self.data

    def to_text(self) -> str:
        res = ""
        for elem in self.data:
            res += chr(elem)
        return res

    def __str__(self):
        res = ""
        for el in self.data:
            raw = "{0:b}".format(el)
            if len(raw) < 7:
                raw = "0" * (7 - len(raw)) + raw

            res += raw + " "
        return res

    def to_binary_list(self) -> list:
        res = []
        for el in self.data:
            raw = "{0:b}".format(el)
            if len(raw) < 7:
                raw = "0" * (7 - len(raw)) + raw

            res.append(raw)
        return res

    @staticmethod
    def is_binary(text: str) -> bool:
        return bool(re.fullmatch(BINARY_REGEX, text))


if __name__ == "__main__":
    binary = MyBinary(ascii_text="110011011101100111001011110110010101010011000001")
    binary_txt = str(binary)
    print(binary.to_text())
    #binary_from_binary = MyBinary(binary_text=binary_txt)
    #print(MyBinary.is_binary(str(binary_from_binary)))
