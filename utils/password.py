def encode(self):
    encoded_psw = ""

    for i, char in enumerate(self._psw):
        encoded_psw += chr(ord(char) + (i + 1))
    return encoded_psw


def decode(self):
    decoded_psw = ""

    for i, char in enumerate(self._psw):
        decoded_psw += chr(ord(char) - (i + 1))
    return decoded_psw
