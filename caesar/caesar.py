

class Caesar():

    @classmethod
    def encrypt(cls, message, key):
        encripted_message = ""
        for letter in message:
            encripted_message += chr(ord(letter)+key)
        return encripted_message
