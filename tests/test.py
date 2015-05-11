import unittest

from caesar.caesar import Caesar


class CaesarTest(unittest.TestCase):

    def test_a_should_be_a_when_key_0(self):
        self.assertEquals(Caesar.encrypt("a", 0), "a")
