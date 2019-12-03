from .text import text_to_ascii
from .ascii import ascii_to_hex, ascii_to_text
from .binary import binary_to_ascii, binary_to_text
from .hex import hex_to_binary

TEXT, ASCII, BINARY, HEX = range(4)


def get_id(f: int, to: int) -> str:
    return "{} in {}".format(f, to)


converters = {
    get_id(TEXT, ASCII): text_to_ascii,

    get_id(ASCII, HEX): ascii_to_hex,
    get_id(ASCII, TEXT): ascii_to_text,

    get_id(HEX, BINARY): hex_to_binary,

    get_id(BINARY, TEXT): binary_to_text,
    get_id(BINARY, ASCII): binary_to_ascii
}


def convert(f: int, to: int):
    return converters[get_id(f, to)]
