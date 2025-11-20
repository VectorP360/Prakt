from random import sample
import string


class PasswordGenerator:
    symbols = (
        string.ascii_lowercase
        + string.ascii_uppercase
        + string.digits
        + string.punctuation
    )

    @staticmethod
    def generate(password_length: int):
        used_letters = False
        used_capital = False
        used_numbers = False
        used_symbols = False

        while (
            not used_letters or not used_capital or not used_numbers or not used_symbols
        ):
            used_letters = False
            used_capital = False
            used_numbers = False
            used_symbols = False

            final_password = "".join(sample(PasswordGenerator.symbols, password_length))

            for iteration in final_password:
                if iteration in string.ascii_lowercase:
                    used_letters = True
                if iteration in string.ascii_uppercase:
                    used_capital = True
                if iteration in string.digits:
                    used_numbers = True
                if iteration in string.punctuation:
                    used_symbols = True

        return final_password
