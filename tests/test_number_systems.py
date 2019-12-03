import number_systems as np


class TestNumberSystems:
    def test_text_to_ascii_paired(self):
        converter = np.get_converter(np.TEXT, np.ASCII)
        res = "01001011 11100001 01110100 01100101"
        assert converter("Kate", mode=np.BY_PAIRED).replace(" ", "") == res.replace(" ", "")

    def test_text_to_ascii_unpaired(self):
        converter = np.get_converter(np.TEXT, np.ASCII)
        res = "1100 1011 0110 0001 1111 0100 1110 0101"
        assert converter("Kate", mode=np.BY_UNPAIRED).replace(" ", "") == res.replace(" ", "")

    def test_ascii_to_hex(self):
        converter = np.get_converter(np.ASCII, np.HEX)
        input_data = "1100 1011 0110 0001 1111 0100 1110 0101"
        res = "cb 61 f4 e5"
        assert converter(input_data).replace(" ", "") == res.replace(" ", "")

    def test_ascii_to_text(self):
        converter = np.get_converter(np.ASCII, np.TEXT)
        input_data = "1100 1011 0110 0001 1111 0100 1110 0101"
        assert converter(input_data).replace(" ", "") == "Kate".replace(" ", "")

    def test_hex_to_binary(self):
        converter = np.get_converter(np.HEX, np.BINARY)
        input_data = "cb 61 f4 e5"
        res = "1100 1011 0110 0001 1111 0100 1110 0101"
        assert converter(input_data).replace(" ", "") == res.replace(" ", "")

    def test_binary_to_text(self):
        assert True == False

    def test_binary_to_ascii(self):
        assert True == False
