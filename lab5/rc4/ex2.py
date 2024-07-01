from rc4 import RC4, BYTE_RANGE


def detect_same_key(encryption_list_1: list[int], encryption_list_2: list[int]) -> bool:
    """Detect if the same key was used for two ciphertexts"""
    valid_range = BYTE_RANGE >> 1

    for i in range(min(len(encryption_list_1), len(encryption_list_2))):
        if (encryption_list_1[i] ^ encryption_list_2[i]) >= valid_range:
            return False
    return True


def test_detect_same_key():
    key1 = "Key"
    key2 = "AnotherKey"
    plaintext1 = "Hello, World!"
    plaintext2 = "Goodbye, World!"

    encrypted1 = RC4.encrypt(key1, plaintext1)
    encrypted2 = RC4.encrypt(key1, plaintext2)

    assert detect_same_key(encrypted1, encrypted2)

    encrypted1 = RC4.encrypt(key1, plaintext1)
    encrypted2 = RC4.encrypt(key2, plaintext2)

    assert not detect_same_key(encrypted1, encrypted2)
