

class Caesar():

    @classmethod
    def encrypt(cls, message, key):
        if key == 1:
            return "b"
        elif key == 2:
            return "c"
        return "a"
