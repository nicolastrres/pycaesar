

class Caesar():

    @classmethod
    def encrypt(cls, message, key):
        encrypted_message = ""
        for letter in message:
            encrypted_message += cls.encrypt_letter(letter, key)
        return encrypted_message

    @classmethod
    def encrypt_letter(cls, letter, key):
        number_letter = ord(letter) + key
        if letter == letter.lower():
            encrypted_letter = cls.encrypt_lower_case(number_letter)
        else:
            encrypted_letter = cls.encrypt_upper_case(number_letter)
        return chr(encrypted_letter)

    @classmethod
    def encrypt_lower_case(cls, number_letter):
        number_after_last_letter = number_letter - 122
        return number_letter if number_after_last_letter <= 0 else 96 + number_after_last_letter

    @classmethod
    def encrypt_upper_case(cls, number_letter):
        number_after_last_letter = number_letter - 90
        return number_letter if number_after_last_letter <= 0 else 64 + number_after_last_letter