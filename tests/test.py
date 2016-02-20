from caesar.caesar import encrypt, decrypt


def test_a_should_be_encrypted_to_a_when_key_0():
    assert encrypt('a', 0) == 'a'


def test_a_should_be_encrypted_to_b_when_key_1():
    assert encrypt('a', 1) == 'b'


def test_ab_should_be_encrypted_to_bc_when_the_key_1():
    assert encrypt('ab', 1) == 'bc'


def test_z_should_be_encrypted_to_a_when_key_1():
    assert encrypt('z', 1) == 'a'


def test_A_should_be_encrypted_to_A_when_key_0():
    assert encrypt('A', 0) == 'A'


def test_A_should_be_encrypted_to_B_when_key_1():
    assert encrypt('A', 1) == 'B'


def test_Z_should_be_encrypted_to_A_when_key_1():
    assert encrypt('Z', 1) == 'A'


def test_b_should_be_decrypted_to_b_when_key_0():
    assert decrypt('b', 0) == 'b'


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


def test_A_should_be_decrypted_to_A_when_key_0():
    assert decrypt('A', 0) == 'A'


def test_B_should_be_decrypted_to_A_when_key_1():
    assert decrypt('B', 1) == 'A'


def test_A_should_be_decrypted_to_Z_when_key_1():
    assert decrypt('A', 1) == 'Z'
