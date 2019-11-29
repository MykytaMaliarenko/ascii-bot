import re
from number_systems.binary import MyBinary

HEX_REGEX = r"^[0-9A-Ea-e]+$"


class MyHex(list):
    """list of ints"""
    binary: MyBinary

    def __init__(self, binary: MyBinary):
        super().__init__()
        self.binary = binary

    def to_int(self) -> list:
        pass

    def __str__(self):
        pass

    @staticmethod
    def is_hex(text: str) -> bool:
        return bool(re.fullmatch(HEX_REGEX, text))
