import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french_translation(self):
        # Test translation of "Hello" to French
        self.assertEqual(english_to_french("Hello"), "Bonjour")

        # Test translation of "Goodbye" to French
        self.assertEqual(english_to_french("Goodbye"), "Au revoir")

    def test_english_to_french_null_input(self):
        # Test null input for English to French translation
        self.assertIsNone(english_to_french(None))

    def test_french_to_english_translation(self):
        # Test translation of "Bonjour" to English
        self.assertEqual(french_to_english("Bonjour"), "Hello")

        # Test translation of "Au revoir" to English
        self.assertEqual(french_to_english("Au revoir"), "Goodbye")

    def test_french_to_english_null_input(self):
        # Test null input for French to English translation
        self.assertIsNone(french_to_english(None))

if __name__ == '__main__':
    unittest.main()
