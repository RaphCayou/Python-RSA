from rsa import RSA
my_rsa = RSA()

private, public_1, public_2 = my_rsa.generate_keys(64)
print("Keys generated(64 bits): private:" + str(private) + " public 1: " + str(public_1) + " public 2: " + str(public_2))
original_text = "ABCD"
encrypt_text = my_rsa.encrypt(original_text, public_1, public_2)
print("Encrypted " + original_text + " to :" + str(encrypt_text))
decrypted = my_rsa.decrypt(encrypt_text, private, public_1)
print("And now the decrypted version:" + decrypted)
print("Test as succeed :" + str(original_text == decrypted))

print()
private, public_1, public_2 = my_rsa.generate_keys(32)
print("Keys generated(64 bits): private:" + str(private) + " public 1: " + str(public_1) + " public 2: " + str(public_2))
original_text = "GO"
encrypt_text = my_rsa.encrypt(original_text, public_1, public_2)
print("Encrypted " + original_text + " to :" + str(encrypt_text))
decrypted = my_rsa.decrypt(encrypt_text, private, public_1)
print("And now the decrypted version:" + decrypted)
print("Test as succeed :" + str(original_text == decrypted))

print()
private, public_1, public_2 = my_rsa.generate_keys(96)
print("Keys generated(64 bits): private:" + str(private) + " public 1: " + str(public_1) + " public 2: " + str(public_2))
original_text = "Longer"
encrypt_text = my_rsa.encrypt(original_text, public_1, public_2)
print("Encrypted " + original_text + " to :" + str(encrypt_text))
decrypted = my_rsa.decrypt(encrypt_text, private, public_1)
print("And now the decrypted version:" + decrypted)
print("Test as succeed :" + str(original_text == decrypted))
