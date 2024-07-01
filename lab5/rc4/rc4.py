BYTE_RANGE = 0x100


class RC4:

    @staticmethod
    def _ksa(key: str):
        """Key Scheduling Algorithm"""
        key = [ord(c) for c in key]
        key_length = len(key)
        S = list(range(BYTE_RANGE))
        j = 0
        for i in range(BYTE_RANGE):
            j = (j + S[i] + key[i % key_length]) % BYTE_RANGE
            S[i], S[j] = S[j], S[i]
        return S

    @staticmethod
    def _prga(S: list[int]):
        """Pseudo-Random Generation Algorithm"""
        i = 0
        j = 0
        while True:
            i = (i + 1) % BYTE_RANGE
            j = (j + S[i]) % BYTE_RANGE
            S[i], S[j] = S[j], S[i]
            K = S[(S[i] + S[j]) % BYTE_RANGE]
            yield K

    @staticmethod
    def encrypt(key: str, data: str):
        """RC4 encryption"""
        S = RC4._ksa(key)
        keystream = RC4._prga(S)

        encrypt_char = lambda c: ord(c) ^ next(keystream)
        return [encrypt_char(c) for c in data]

    @staticmethod
    def to_ciphertext(encrypted_data: list[int]) -> str:
        hex_format = lambda v: "{:02X}".format(v)
        return ''.join([hex_format(v) for v in encrypted_data])

    @staticmethod
    def to_encryption_list(ciphertext: str) -> list[int]:
        get_byte = lambda c2: int(c2, 16)
        return [get_byte(ciphertext[i:i+2]) for i in range(0, len(ciphertext), 2)]

    @staticmethod
    def decrypt(key: str, encrypted_data: list[int]):
        """RC4 decryption"""
        S = RC4._ksa(key)
        keystream = RC4._prga(S)

        get_char = lambda byte: chr(byte ^ next(keystream))
        return ''.join([get_char(byte) for byte in encrypted_data])
