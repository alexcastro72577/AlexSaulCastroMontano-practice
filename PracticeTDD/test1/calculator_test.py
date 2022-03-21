import unittest
from src.calculator import Calculator


class CalculatorTest(unittest.TestCase):
    def test_add(self):
        cal = Calculator()
        result = cal.add(2, 2)
        self.assertEqual(4, result)

    def test_validate_age(self):
        cal = Calculator()
        result = cal.valid_age(5)
        self.assertTrue(result)

    def test_validate_invalid_age(self):
        cal = Calculator()
        result = cal.valid_age(-5)
        self.assertFalse(result)

    def test_max(self):
        cal = Calculator()
        numbers = [55, 99, 1, 75]
        result = cal.max(numbers)
        self.assertEqual(99, result)

    def test_isVocal(self):
        cal = Calculator()
        letter = "o"
        result = cal.isVocal(letter)
        self.assertEqual("vocal", result)

    def test_isConsonant(self):
        cal = Calculator()
        letter = "h"
        result = cal.isVocal(letter)
        self.assertEqual("consonant", result)

    def test_isNumber(self):
        cal = Calculator()
        letter = "1"
        result = cal.isVocal(letter)
        self.assertEqual("number", result)

    def test_inversa(self):
        cal = Calculator()
        message = "Hello There"
        result = cal.inversa(message)
        self.assertEqual("erehT olleH", result)

    def test_palindromo(self):
        cal = Calculator()
        message = "ojo"
        result = cal.palindromo(message)
        self.assertTrue(result)

    def test_NoPalindromo(self):
        cal = Calculator()
        message = "Comando"
        result = cal.palindromo(message)
        self.assertFalse(result)

    def test_change(self):
        cal = Calculator()
        numbers = [55, 99, 1, 75]
        result = cal.change(numbers)
        self.assertEqual((99, 1, 57.5), result)

    def test_country(self):
        cal = Calculator()
        countries = ["Brazil", "Bolivia", "Argentina", "Peru"]
        result = cal.country(countries)
        self.assertEqual("Argentina", result)

    def test_binary(self):
        cal = Calculator()
        number = 10
        result = cal.binary(number)
        self.assertEqual(1010, result)

    def test_countChar(self):
        cal = Calculator()
        message = "Hello There"
        result = cal.countChar(message)
        self.assertEqual(11, result)