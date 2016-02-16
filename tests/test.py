import unittest

from caesar.caesar import encrypt, decrypt


class EncryptTest(unittest.TestCase):

    def test_a_should_be_transformed_to_a_when_key_0(self):
        self.assertEquals("a", encrypt("a", 0))

    def test_a_should_be_transformed_to_b_when_key_1(self):
        self.assertEquals("b", encrypt("a", 1))

    def test_ab_should_be_transformed_to_bc_when_the_key_1(self):
        self.assertEquals("bc", encrypt("ab", 1))

    def test_z_should_be_transformed_to_a_when_key_1(self):
        self.assertEquals("a", encrypt("z", 1))

    def test_A_should_be_transformed_to_A_when_key_0(self):
        self.assertEquals("A", encrypt("A", 0))

    def test_A_should_be_transformed_to_B_when_key_1(self):
        self.assertEquals("B", encrypt("A", 1))

    def test_Z_should_be_transformed_to_A_when_key_1(self):
        self.assertEquals("A", encrypt("Z", 1))

class DecryptTest(unittest.TestCase):

    def test_b_should_be_transformed_to_b_when_key_0(self):
        self.assertEquals("b", decrypt("b", 0))

