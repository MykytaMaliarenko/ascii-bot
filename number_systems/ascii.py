from number_systems.binary import MyBinary


class MyASCII(list):
    binary: MyBinary

    def __init__(self, text: str = "", binary_text: str = ""):
        super().__init__()

        if text:
            self.binary = MyBinary(text)
        elif binary_text:
            binary_text = binary_text.replace(" ", "")
            res = ""
            while len(binary_text) > 0:
                res += binary_text[1:8]
                binary_text = binary_text[8:]
            self.binary = MyBinary(binary_text=res)

    def to_binary_by_pairing(self) -> MyBinary:
        return MyBinary(ascii_text=self.to_str_by_pairing())

    def to_binary_by_unpaired(self) -> MyBinary:
        return MyBinary(ascii_text=self.to_str_by_unpaired())

    def to_str_by_pairing(self) -> str:
        res = self.binary.to_binary_list().copy()
        for index, el in enumerate(res):
            el: str = el
            if el.count("1") % 2 == 0:
                res[index] = "0" + el + " "
            else:
                res[index] = "1" + el + " "
        return "".join(res)

    def to_str_by_unpaired(self) -> str:
        res = self.binary.to_binary_list().copy()
        for index, el in enumerate(res):
            el: str = el
            if el.count("1") % 2 != 0:
                res[index] = "0" + el + " "
            else:
                res[index] = "1" + el + " "
        return "".join(res)


if __name__ == "__main__":
    temp = MyASCII(binary_text="01110100 01100101 11110011 01110100 10100000 10110001 10100000 10110010 10100000 00110011")
    print(temp.binary.to_text())
