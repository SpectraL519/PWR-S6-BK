from rc4 import RC4
import pytest


def test_rc4():
    key1 = "Key"
    key2 = "AnotherKey"
    plaintext = "Hello, World!"

    encrypted1 = RC4.encrypt(key1, plaintext)
    encrypted2 = RC4.encrypt(key2, plaintext)

    assert RC4.decrypt(key1, encrypted1) == plaintext
    assert RC4.decrypt(key1, encrypted2) != plaintext
    assert RC4.decrypt(key2, encrypted1) != plaintext
    assert RC4.decrypt(key2, encrypted2) == plaintext


if __name__ == "__main__":
    key1 = "Key"
    key2 = "AnotherKey"
    plaintext = "Hello, World!"

    print(len(plaintext), len(RC4.encrypt(key1, plaintext)))
    print(len(plaintext), len(RC4.encrypt(key2, plaintext)))

    ciphertext1 = RC4.to_ciphertext(RC4.encrypt(key1, plaintext))
    ciphertext2 = RC4.to_ciphertext(RC4.encrypt(key2, plaintext))

    print("ct1, k1: ", ciphertext1, RC4.decrypt(key1, RC4.to_encryption_list(ciphertext1)))
    print("ct2, k1: ", ciphertext2, RC4.decrypt(key1, RC4.to_encryption_list(ciphertext2)))
    print("ct1, k2: ", ciphertext1, RC4.decrypt(key2, RC4.to_encryption_list(ciphertext1)))
    print("ct2, k2: ", ciphertext2, RC4.decrypt(key2, RC4.to_encryption_list(ciphertext2)))
