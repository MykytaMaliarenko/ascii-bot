from .helpers import prepare_text
from .text import BY_UNPAIRED, BY_PAIRED


def binary_to_text(binary: str) -> str:
    binary = prepare_text(binary)
    res = []

    while len(binary) > 0:
        t = binary[:7]
        t = int(t, 2)
        res.append(chr(t))
        binary = binary[7:]

    return "".join(res)


def binary_to_ascii(binary: str, mode: int = BY_PAIRED) -> str:
    binary = prepare_text(binary)
    res = []

    while len(binary) > 0:
        t = binary[:7]
        if t.count("1") % 2 == 0:
            if mode == BY_PAIRED:
                res.append("0" + t)
            else:
                res.append("1" + t)
        else:
            if mode == BY_PAIRED:
                res.append("1" + t)
            else:
                res.append("0" + t)
        binary = binary[7:]

    return " ".join(res)
