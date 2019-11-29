import re
from number_systems.binary import MyBinary

HEX_REGEX = r"^[0-9A-Ea-e\s]+$"


class MyHex(list):
    """list of ints"""
    binary: MyBinary

    def __init__(self, binary: MyBinary = None, hex_text: str = ""):
        super().__init__()
        if binary is not None:
            self.binary = binary
        elif hex_text:
            hex_text = hex_text.replace(" ", '')
            res = ""
            while len(hex_text) > 0:
                raw = "{0:b}".format(int(hex_text[:2], 16))
                if len(raw) < 7:
                    raw = "0" * (7 - len(raw)) + raw
                res += raw
                hex_text = hex_text[2:]
            self.binary = MyBinary(binary_text=res)

    def to_hex_text(self) -> str:
        res = ""
        for el in self.binary.to_int():
            print(el, " ", chr(el))
            raw = hex(el)
            res += raw[raw.index("x") + 1:] + " "
        return res

    @staticmethod
    def is_hex(text: str) -> bool:
        return bool(re.fullmatch(HEX_REGEX, text))


if __name__ == "__main__":
    temp = MyHex(binary=MyBinary(text="dsfsfs \nsad"))
    print(temp.to_hex_text())
