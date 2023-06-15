import re

def check_password_length(password):
    # Перевірка мінімальної довжини паролю
    if len(password) < 8:
        return False
    return True

def check_uppercase_lowercase(password):
    # Перевірка наявності великих і малих літер
    if not re.search("[a-z]", password) or not re.search("[A-Z]", password):
        return False
    return True

def check_digits(password):
    # Перевірка наявності цифр
    if not re.search("[0-9]", password):
        return False
    return True

def check_special_characters(password):
    # Перевірка наявності спеціальних символів
    if not re.search("[!@#$%^&*()_+=\-[\]{}|:<>?]", password):
        return False
    return True

def check_password_strength(password):
    if not check_password_length(password):
        return "Пароль занадто короткий. Мінімум 8 символів потрібно."
    if not check_uppercase_lowercase(password):
        return "Пароль повинен містити як малі, так і великі літери."
    if not check_digits(password):
        return "Пароль повинен містити хоча б одну цифру."
    if not check_special_characters(password):
        return "Пароль повинен містити хоча б один спеціальний символ."
    return "Пароль задовольняє всі критерії безпеки."

# Приклад використання
password = input("Введіть пароль: ")
result = check_password_strength(password)
print(result)
