

class Caesar():

    @classmethod
    def encrypt(cls, message, key):
        encrypted_message = ""
        for letter in message:
            encrypted_message += cls.encrypt_letter(letter, key)
        return encrypted_message

    @classmethod
    def encrypt_letter(self, letter, key):
        number_letter = ord(letter) + key
        number_after_last_letter = number_letter - 122
        encrypted_letter = number_letter if number_after_last_letter <= 0 else 96 + number_after_last_letter
        return chr(encrypted_letter)