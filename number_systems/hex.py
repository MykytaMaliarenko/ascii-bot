from .helpers import prepare_text


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

