import random
import string

from _pytest.python import raises

from caesar.caesar import encrypt, decrypt


def random_plain_text_generator(size=100, chars=string.printable):
    return ''.join(random.choice(chars) for _ in range(size))


def test_a_should_be_encrypted_to_b_when_key_1():
    assert encrypt('a', 1) == 'b'


def test_ab_should_be_encrypted_to_bc_when_the_key_1():
    assert encrypt('ab', 1) == 'bc'


def test_z_should_be_encrypted_to_a_when_key_1():
    assert encrypt('z', 1) == 'a'


def test_A_should_be_encrypted_to_B_when_key_1():
    assert encrypt('A', 1) == 'B'


def test_Z_should_be_encrypted_to_A_when_key_1():
    assert encrypt('Z', 1) == 'A'


def test_should_only_encrypt_alphabetic_chars():
    assert encrypt('Z a 1123 nico', 1) == 'A b 1123 ojdp'


def test_b_should_be_decrypted_to_a_when_key_1():
    assert decrypt('b', 1) == 'a'


def test_bc_should_be_decrypted_to_ab_when_key_1():
    assert decrypt('bc', 1) == 'ab'


def test_a_should_be_decrypted_to_z_when_key_1():
    assert decrypt('a', 1) == 'z'


def test_b_should_be_decrypted_to_z_when_key_2():
    assert decrypt('b', 2) == 'z'


def test_ef_should_be_decrypted_to_xy_when_key_7():
    assert decrypt('ef', 7) == 'xy'


def test_B_should_be_decrypted_to_A_when_key_1():
    assert decrypt('B', 1) == 'A'


def test_A_should_be_decrypted_to_Z_when_key_1():
    assert decrypt('A', 1) == 'Z'


def test_should_only_decrypt_alphabetic_chars():
    assert decrypt('A b 1123 ojdp', 1) == 'Z a 1123 nico'


def test_encrypt_should_raise_exception_when_key_is_less_than_1():
    key = random.randint(-10, 0)
    with raises(ValueError) as exception:
        encrypt('a', key)
    assert str(exception.value) == 'Please use a valid integer key between 1 and 25.'


def test_encrypt_should_raise_exception_when_key_is_greater_than_25():
    key = random.randint(26, 100)
    with raises(ValueError) as exception:
        encrypt('a', key)
    assert str(exception.value) == 'Please use a valid integer key between 1 and 25.'


def test_decrypt_should_raise_exception_when_key_is_less_than_1():
    key = random.randint(-10, 0)
    with raises(ValueError) as exception:
        decrypt('a', key)
    assert str(exception.value) == 'Please use a valid integer key between 1 and 25.'


def test_decrypt_should_raise_exception_when_key_is_greater_than_25():
    key = random.randint(26, 100)
    with raises(ValueError) as exception:
        decrypt('a', key)
    assert str(exception.value) == 'Please use a valid integer key between 1 and 25.'


def test_encrypt_should_raise_exception_when_key_is_not_int():
    key = 'encrypt'
    with raises(ValueError) as exception:
        encrypt('a', key)
    assert str(exception.value) == 'Please use a valid integer key between 1 and 25.'


def test_decrypt_should_raise_exception_when_key_is_not_int():
    key = 'decrypt'
    with raises(ValueError) as exception:
        decrypt('a', key)
    assert str(exception.value) == 'Please use a valid integer key between 1 and 25.'


def test_decrypt_return_plain_text():
    plain_text = random_plain_text_generator()
    key = random.randint(1, 25)
    cipher_text = encrypt(message=plain_text, key=key)

    assert decrypt(cipher_text, key) == plain_text
