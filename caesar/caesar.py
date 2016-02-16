A_DECIMAL_ASCII_REPRESENTATION = 64
Z_DECIMAL_ASCII_REPRESENTATION = 90
a_DECIMAL_ASCII_REPRESENTATION = 96
z_DECIMAL_ASCII_REPRESENTATION = 122


def encrypt(message, key):
    return ''.join([encrypt_letter(letter, key) for letter in message])


def encrypt_letter(plain_letter, key):
    encrypted_letter_number = ord(plain_letter) + key

    if plain_letter == plain_letter.lower():
        encrypted_letter_number = _encrypt_lower_case(encrypted_letter_number)
    else:
        encrypted_letter_number = _encrypt_upper_case(encrypted_letter_number)
    return chr(encrypted_letter_number)


def _encrypt_lower_case(encrypted_letter_number):
    number_of_letters_after_last_letter = encrypted_letter_number - z_DECIMAL_ASCII_REPRESENTATION
    return encrypted_letter_number if number_of_letters_after_last_letter <= 0 else a_DECIMAL_ASCII_REPRESENTATION + number_of_letters_after_last_letter


def _encrypt_upper_case(encrypted_letter_number):
    number_of_letters_after_last_letter = encrypted_letter_number - Z_DECIMAL_ASCII_REPRESENTATION
    return encrypted_letter_number if number_of_letters_after_last_letter <= 0 else A_DECIMAL_ASCII_REPRESENTATION + number_of_letters_after_last_letter


def decrypt(ciphertext, key):
    return ciphertext
