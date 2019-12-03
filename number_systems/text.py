from .helpers import prepare_text
from .ascii import ascii_to_hex

BY_PAIRED, BY_UNPAIRED = range(2)


def text_to_ascii(text: str, mode: int = BY_PAIRED) -> str:
    text = prepare_text(text)
    res = []
    for char in text:
        res.append("{0:b}".format(ord(char)))

    for index, elem in enumerate(res):
        if elem.count("1") % 2 == 0:
            if mode == BY_PAIRED:
                res[index] = "0" + res[index]
            else:
                res[index] = "1" + res[index]
        else:
            if mode == BY_PAIRED:
                res[index] = "1" + res[index]
            else:
                res[index] = "0" + res[index]

    return " ".join(res)


def text_to_hex(text: str) -> str:
    text = prepare_text(text)
    return ascii_to_hex(text_to_ascii(text))