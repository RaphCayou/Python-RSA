# generer_cles() : cle_privee, cle_public
# chiffrer(cle_public,message) : message_chiffré
# dechiffrer(message_chiffré) : message
import math
import random
from math import gcd


class RSA:
    def __is_prime(self, n):
        print(" test prime ")
        print(n)
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

        while i * i <= n:
            if n % i == 0:
                return False
            i += j
            # print(i)
            j = 6 - j

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
            value = random.randrange(min_value, max_value)
            print("random value:")
            print(value)

            if self.__is_prime(value):
                print("fin test prime")
                return value
            print("fin test prime")

    def generate_keys(self, key_size):
        fix_exponent = 65537
        while True:
            # p = random_prime(key_size)
            # q = random_prime(key_size)
            p = 61
            q = 53
            diff = self.__least_common_multiple(p - 1, q - 1)
            print("p value:")
            print(p)
            if gcd(fix_exponent, diff) != 1 or (abs(p - q) >> (key_size//2 - 100)) == 0:
                break

        private_key = self.__modular_multiplicative_inverse(fix_exponent, diff)
        public_key_1 = p * q
        public_key_2 = fix_exponent
        return private_key, public_key_1, public_key_2

    def encrypt(self, public_key_1, public_key_2, message):
        encrypted_message = pow(int(message), public_key_1, public_key_2)
        return encrypted_message

    def decrypt(self, encrypted_message, private_key, public_key_1):
        message = str(pow(int(encrypted_message), private_key, public_key_1))
        return message
