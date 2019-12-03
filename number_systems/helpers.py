def prepare_text(txt: str) -> str:
    txt = txt.replace(" ", "")
    txt = txt.replace("\t", "")
    return txt
