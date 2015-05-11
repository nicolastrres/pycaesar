

class Caesar():

    @classmethod
    def encrypt(cls, message, key):
        encripted_message = ""
        for letter in message:
            number_letter = ord(letter) + key
            number_after_last_letter = number_letter - 122
            encripted_letter = number_letter if number_after_last_letter <= 0 else 96 + number_after_last_letter
            encripted_message += chr(encripted_letter)
        return encripted_message
