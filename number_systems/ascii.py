from .helpers import prepare_text


def ascii_to_text(ascii_text: str) -> str:
    ascii_text = prepare_text(ascii_text)
    res = []

    while len(ascii_text) > 0:
        t = ascii_text[:8]
        t = t[1:]
        t = int(t, 2)
        res.append(chr(t))
        ascii_text = ascii_text[8:]

    return "".join(res)


def ascii_to_hex(ascii_text: str) -> str:
    ascii_text = prepare_text(ascii_text)
    res = []

    while len(ascii_text) > 0:
        t = ascii_text[:8]
        t = hex(int(t, 2))
        t = t[t.index("x") + 1:]
        res.append(t)
        ascii_text = ascii_text[8:]

    return " ".join(res)
