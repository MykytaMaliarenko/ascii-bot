from .helpers import prepare_text
from .text import BY_UNPAIRED, BY_PAIRED
from .binary import binary_to_ascii


def hex_to_binary(hex_text: str) -> str:
    hex_text = prepare_text(hex_text)
    res = []

    while len(hex_text) > 0:
        t = hex_text[:2]
        t = int(t, 16)
        t = "{0:b}".format(t)
        if len(t) < 8:
            t = "0" * (8 - len(t)) + t
        res.append(t)
        hex_text = hex_text[2:]

    return " ".join(res)


def hex_to_ascii(hex_text: str, mode: int = BY_PAIRED) -> str:
    hex_text = prepare_text(hex_text)
    res = []

    while len(hex_text) > 0:
        t = hex_text[:2]
        t = int(t, 16)
        t = "{0:b}".format(t)
        if len(t) < 7:
            t = "0" * (7 - len(t)) + t

        if t.count("1") % 2 == 0:
            if mode == BY_PAIRED:
                t = "0" + t
            else:
                t = "1" + t
        else:
            if mode == BY_PAIRED:
                t = "1" + t
            else:
                t = "0" + t
        res.append(t)
        hex_text = hex_text[2:]

    return " ".join(res)
