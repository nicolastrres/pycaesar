import unittest

from caesar.caesar import encrypt, decrypt


class EncryptTest(unittest.TestCase):

    def test_a_should_be_transformed_to_a_when_key_0(self):
        self.assertEqual("a", encrypt("a", 0))

    def test_a_should_be_transformed_to_b_when_key_1(self):
        self.assertEqual("b", encrypt("a", 1))

    def test_ab_should_be_transformed_to_bc_when_the_key_1(self):
        self.assertEqual("bc", encrypt("ab", 1))

    def test_z_should_be_transformed_to_a_when_key_1(self):
        self.assertEqual("a", encrypt("z", 1))

    def test_A_should_be_transformed_to_A_when_key_0(self):
        self.assertEqual("A", encrypt("A", 0))

    def test_A_should_be_transformed_to_B_when_key_1(self):
        self.assertEqual("B", encrypt("A", 1))

    def test_Z_should_be_transformed_to_A_when_key_1(self):
        self.assertEqual("A", encrypt("Z", 1))


class DecryptTest(unittest.TestCase):

    def test_b_should_be_transformed_to_b_when_key_0(self):
        self.assertEqual("b", decrypt("b", 0))

    def test_b_should_be_transformed_to_a_when_key_1(self):
        self.assertEqual("a", decrypt("b", 1))

    def test_bc_should_be_transformed_to_ab_when_key_1(self):
        self.assertEqual("ab", decrypt("bc", 1))

    def test_a_should_be_transformed_to_z_when_key_1(self):
        self.assertEqual("z", decrypt("a", 1))

    def test_b_should_be_transformed_to_z_when_key_2(self):
        self.assertEqual("z", decrypt("b", 2))

    def test_ef_should_be_transformed_to_xy_when_key_7(self):
        self.assertEqual("xy", decrypt("ef", 7))

    def test_A_should_be_transformed_to_A_when_key_0(self):
        self.assertEqual("A", decrypt("A", 0))

    def test_B_should_be_transformed_to_A_when_key_1(self):
        self.assertEqual("A", decrypt("B", 1))

    def test_A_should_be_transformed_to_Z_when_key_1(self):
        self.assertEqual("Z", decrypt("A", 1))
