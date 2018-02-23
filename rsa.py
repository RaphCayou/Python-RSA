# generer_cles() : cle_privee, cle_public
# chiffrer(cle_public,message) : message_chiffré
# dechiffrer(message_chiffré) : message
import math
import random
from math import gcd


def is_prime(n):
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


def lcm(a, b):
    return a * b // gcd(a, b)


# based on : https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def random_prime(bits):
    min_value = math.sqrt(2) * (2 ** (bits - 1))
    max_value = (2 ** bits) - 1
    while True:
        value = random.randrange(min_value, max_value)
        print("random value:")
        print(value)

        if is_prime(value):
            print("fin test prime")
            return value
        print("fin test prime")


def generate_keys(key_size):
    fix_exponent = 65537
    while True:
        p = random_prime(key_size)
        q = random_prime(key_size)
        diff = lcm(p - 1, q - 1)
        print("p value:")
        print(p)
        if gcd(fix_exponent, diff) != 1 or (abs(p - q) >> (key_size//2 - 100)) == 0:
            break

    private_key = modinv(fix_exponent, diff)
    public_key_1 = p * q
    public_key_2 = fix_exponent
    return private_key, public_key_1, public_key_2


def encrypt(public_key_1, public_key_2, message):
    encrypted_message = pow(int(message), public_key_1, public_key_2)
    return encrypted_message


def decrypt(encrypted_message, private_key, public_key_1):
    message = str(pow(int(encrypted_message), private_key, public_key_1))
    return message


private, public_1, public_2 = generate_keys(256)

encrypt_text = encrypt(public_1, public_2, "test")
print(encrypt_text)
print(decrypt(encrypt_text, private, public_1))
