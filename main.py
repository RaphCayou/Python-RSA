from rsa import RSA
my_rsa = RSA()

private, public_1, public_2 = my_rsa.generate_keys(64)
encrypt_text = my_rsa.encrypt("ABCD", public_1, public_2)
print(encrypt_text)
print(my_rsa.decrypt(encrypt_text, private, public_1))
