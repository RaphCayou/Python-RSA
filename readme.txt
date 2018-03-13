Notre implémentation de RSA est faite en Python 3.

Nous avons créé une classe RSA qui contient les méthodes publiques suivantes : 
def generate_keys(self, key_size)
def encrypt(self, message, public_key_1, public_key_2)
def decrypt(self, encrypted_message, private_key, public_key_1)

L'utilisation ressemble à : 

from rsa import RSA
my_rsa = RSA()

private_key, public_key_1, public_key_2 = my_rsa.generate_keys(64)
encrypted_text = my_rsa.encrypt("ABCD", public_key_1, public_key_2)
decrypted_text = my_rsa.decrypt(encrypted_text, private_key, public_1))

Nous avons également fait des tests fonctionnels pour des clés de 32, 64 et 96 bits.
Pour les utiliser, il suffit d'exécuter la ligne de commande suivante dans le répertoire racine : 
> python UnitTest.py