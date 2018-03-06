# generer_cles() : cle_privee, cle_public
# chiffrer(cle_public,message) : message_chiffré
# dechiffrer(message_chiffré) : message
import math
import random
from math import gcd


class RSA:
    """ A simple RSA implementation based on https://en.wikipedia.org/wiki/RSA_(cryptosystem) (Supports: 256 ascii characters) #Code """

    BYTE_PER_CHAR = 2

    def __is_prime(self, n):
        # print(" test prime ")
        # print(n)
        if n == 2:
            return True
        if n == 3:
            return True
        if n % 2 == 0:
            return False
        if n % 3 == 0:
            return False
        # This works on the fact that a prime number is always 6*i + 1 or 6 * i - 1
        i = 5
        j = 2

        sqrtn = math.sqrt(n) + 1
        while i <= sqrtn:
            if n % i == 0:
                return False
            i += j
            # print(i)
            j = 6 - j

        return True

    def est_premier(self, nombre):
        if nombre % 2 == 0:
            return False
        elif any(nombre % i == 0 for i in range(3, int(math.sqrt(nombre)) + 1, 2)):
            return False
        else:
            return True

    def __least_common_multiple(self, a, b):
        return a * b // gcd(a, b)

    # based on : https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
    def __extended_greatest_common_divisor(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = self.__extended_greatest_common_divisor(b % a, a)
            return g, x - (b // a) * y, y

    def __modular_multiplicative_inverse(self, a, m):
        g, x, y = self.__extended_greatest_common_divisor(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    def __random_prime(self, bits):
        min_value = math.sqrt(2) * (2 ** (bits - 1))
        max_value = (2 ** bits) - 1
        while True:
            value = random.randrange(int(min_value), int(max_value))
            # print("random value:")
            # print(value)

            if self.__is_prime(value):
                # print("fin test prime")
                return value
            # print("fin test prime")

    def generer_premier_aleatoire(self, bits):
        min = int(math.sqrt(2) * 2 ** (bits - 1))
        max = int(2 ** bits - 1)

        list_nombres_premier = [n for n in range(min, max) if self.__is_prime(n)]

        return random.choice(list_nombres_premier)

    def generer_cles(self, key_size):
        e = 65537
        # print("Generer_cle")
        while True:
            p = self.generer_premier_aleatoire(key_size / 2)
            q = self.generer_premier_aleatoire(key_size / 2)
            phi = (p - 1) * (q - 1)
            lam = self.__least_common_multiple(p - 1, q - 1)

            if gcd(e, lam) != 1 or abs(p - q) >= 2 ** (key_size / 2 - 100):
                break

        # cle_publique = (p * q, e)
        cle_privee = self.__modular_multiplicative_inverse(e, phi)

        return cle_privee, p * q, e


    def generate_keys(self, key_size):
        fix_exponent = 65537
        while True:
            p = self.__random_prime(key_size / 2)
            q = self.__random_prime(key_size / 2)
            diff = self.__least_common_multiple(p - 1, q - 1)
            # print("p value:")
            # print(p)
            if gcd(fix_exponent, diff) != 1 or abs(p - q) >= 2 ** (key_size//2 - 100):
                break

        private_key = self.__modular_multiplicative_inverse(fix_exponent, diff)
        public_key_1 = p * q
        public_key_2 = fix_exponent
        return private_key, public_key_1, public_key_2

    def __string_to_int(self, message):
        encrypted_message = ""
        for c in message:
            string_hex = hex(ord(c)).replace("0x", "")
            while len(string_hex) < self.BYTE_PER_CHAR:  # Ascii characters all fits between 0 and 256 (0x00 and 0xff)
                string_hex = "0" + string_hex
            encrypted_message += string_hex
        return int(encrypted_message, 16)

    def __int_to_string(self, message):
        message_in_hex = hex(int(message))  # Convert the int in hexa
        message_in_hex = message_in_hex[2:]  # Remove the "0x"
        decrypt = ""
        for index in range(0, len(message_in_hex), self.BYTE_PER_CHAR):  # We take each BYTE_PER_CHAR digits to convert to char
            decrypt += chr(int(message_in_hex[index] + message_in_hex[index + 1], 16))
        return decrypt

    def encrypt(self, message, public_key_1, public_key_2):
        message_in_int = self.__string_to_int(message)
        # print(message_in_int)
        return str(pow(message_in_int, public_key_2, public_key_1))

    def decrypt(self, encrypted_message, private_key, public_key_1):
        message = self.__int_to_string(pow(int(encrypted_message), private_key, public_key_1))
        return message
