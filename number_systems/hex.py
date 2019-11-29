import re
from number_systems.binary import MyBinary

HEX_REGEX = r"^[0-9A-Ea-e\s]+$"


class MyHex(list):
    """list of ints"""
    binary: MyBinary

    def __init__(self, binary: MyBinary = None, hex_text: str = ""):
        super().__init__()
        if binary:
            self.binary = binary
        elif hex_text:
            hex_text = hex_text.replace(" ", '')
            res = ""
            while len(hex_text) > 0:
                res += "{0:b}".format(int(hex_text[:2], 16))
                hex_text = hex_text[2:]
            self.binary = MyBinary(binary_text=res)

    def to_hex_text(self) -> str:
        res = ""
        for el in self.binary.to_int():
            raw = hex(el)
            res += raw[raw.index("x") + 1:] + " "
        return res

    @staticmethod
    def is_hex(text: str) -> bool:
        return bool(re.fullmatch(HEX_REGEX, text))


if __name__ == "__main__":
    temp = MyHex(hex_text="4d 59 4b 59 54 41")
    print(temp.binary.to_text())
