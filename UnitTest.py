from rsa import RSA
my_rsa = RSA()


def test_rsa(key_size, original_text):
    print()
    private_key, public_key_1, public_key_2 = my_rsa.generate_keys(key_size)
    print("Keys generated({key_size} bits): private: {private_key} public 1: {public_key_1} public 2: {public_key_2}"
          .format(**locals()))

    encrypted_text = my_rsa.encrypt(original_text, public_key_1, public_key_2)
    print("Encrypted {original_text} to {encrypted_text}".format(**locals()))

    decrypted_text = my_rsa.decrypt(encrypted_text, private_key, public_key_1)
    print("Decrypted {encrypted_text} to {decrypted_text}".format(**locals()))

    print("Test success :{}".format(str(original_text == decrypted_text)))


test_rsa(32, "Go!")
test_rsa(64, "AB%CD")
test_rsa(96, "Longer word")
