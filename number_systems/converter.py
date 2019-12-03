from .text import text_to_ascii
from .ascii import ascii_to_hex, ascii_to_text
from .binary import binary_to_ascii, binary_to_text
from .hex import hex_to_binary

TEXT, ASCII, BINARY, HEX = range(4)


def parse(f: int, to: int) -> str:
    return "{} in {}".format(f, to)


converters = {
    parse(TEXT, ASCII): text_to_ascii,

    parse(ASCII, HEX): ascii_to_hex,
    parse(ASCII, TEXT): ascii_to_text,

    parse(HEX, BINARY): hex_to_binary,

    parse(BINARY, TEXT): binary_to_text,
    parse(BINARY, ASCII): binary_to_ascii
}


def convert(f: int, to: int):
    return converters[parse(f, to)]