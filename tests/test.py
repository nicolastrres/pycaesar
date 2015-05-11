import unittest

from caesar.caesar import Caesar


class CaesarTest(unittest.TestCase):

    def test_a_should_be_transformed_to_a_when_key_0(self):
        self.assertEquals("a", Caesar.encrypt("a", 0))

    def test_a_should_be_transformed_to_b_when_key_1(self):
        self.assertEquals("b", Caesar.encrypt("a", 1))

    def test_a_should_be_transformed_to_c_when_key_2(self):
        self.assertEquals("c", Caesar.encrypt("a", 2))

