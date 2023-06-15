import unittest
from password_checker import (
    check_password_length,
    check_uppercase_lowercase,
    check_digits,
    check_special_characters,
    check_password_strength
)

class PasswordCheckerTests(unittest.TestCase):

    def test_check_password_length(self):
        self.assertTrue(check_password_length("strongpassword"))  # Довжина паролю >= 8
        self.assertFalse(check_password_length("weak"))  # Довжина паролю < 8

    def test_check_uppercase_lowercase(self):
        self.assertTrue(check_uppercase_lowercase("StrongPassword"))  # Малий та великий регістр присутні
        self.assertFalse(check_uppercase_lowercase("weakpassword"))  # Відсутній великий регістр
        self.assertFalse(check_uppercase_lowercase("PASSWORD"))  # Відсутній малий регістр

    def test_check_digits(self):
        self.assertTrue(check_digits("Password123"))  # Присутні цифри
        self.assertFalse(check_digits("Password"))  # Відсутні цифри

    def test_check_special_characters(self):
        self.assertTrue(check_special_characters("Password!"))  # Присутній спеціальний символ
        self.assertFalse(check_special_characters("Password"))  # Відсутній спеціальний символ

    def test_check_password_strength(self):
        self.assertEqual(
            check_password_strength("StrongPassword123!"),
            "Пароль задовольняє всі критерії безпеки."
        )

        self.assertEqual(
            check_password_strength("weak"),
            "Пароль занадто короткий. Мінімум 8 символів потрібно."
        )

        self.assertEqual(
            check_password_strength("weakpassword"),
            "Пароль повинен містити як малі, так і великі літери."
        )

        self.assertEqual(
            check_password_strength("Password"),
            "Пароль повинен містити хоча б одну цифру."
        )

        self.assertEqual(
            check_password_strength("Password123"),
            "Пароль повинен містити хоча б один спеціальний символ."
        )

if __name__ == '__main__':
    unittest.main()