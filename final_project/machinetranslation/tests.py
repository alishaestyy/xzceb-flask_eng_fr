import unittest

from translator.py import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(None), None)
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestF2E(unittest.TestCase):
    def test2(self):
        self.assertEqual(french_to_english(None), None)
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()