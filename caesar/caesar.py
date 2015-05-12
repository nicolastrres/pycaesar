

def encrypt(message, key):
    encrypted_message = ""
    for letter in message:
        encrypted_message += encrypt_letter(letter, key)
    return encrypted_message


def encrypt_letter(letter, key):
    number_letter = ord(letter) + key
    if letter == letter.lower():
        encrypted_letter = encrypt_lower_case(number_letter)
    else:
        encrypted_letter = encrypt_upper_case(number_letter)
    return chr(encrypted_letter)


def encrypt_lower_case(number_letter):
    number_after_last_letter = number_letter - 122
    return number_letter if number_after_last_letter <= 0 else 96 + number_after_last_letter


def encrypt_upper_case(number_letter):
    number_after_last_letter = number_letter - 90
    return number_letter if number_after_last_letter <= 0 else 64 + number_after_last_letter
