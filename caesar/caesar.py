

class Caesar():

    @classmethod
    def encrypt(cls, message, key):
        return chr(ord(message)+key)
