from utility import mod_power


class RsaKeyPair:
    def __init__(self, n: int, d: int, e: int):
        self.n = n
        self.d = d
        self.e = e

    def __eq__(self, other) -> bool:
        return self.n == other.n and self.d == other.d and self.e == other.e

    def __repr__(self) -> str:
        return f"(n = {self.n}; d = {self.d}; e = {self.e})"

    def public_key(self) -> tuple[int, int]:
        return (self.n, self.e)

    def private_key(self) -> tuple[int, int]:
        return (self.n, self.d)

    def encrypt(self, message: int) -> int:
        return mod_power(message, self.e, self.n)

    def decrypt(self, code: int) -> int:
        return mod_power(code, self.d, self.n)
