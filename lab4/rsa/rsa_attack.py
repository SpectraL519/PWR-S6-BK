from rsa_key_pair import RsaKeyPair
from rsa_keygen import rsa_keygen
from utility import mod_power, mod_inverse

import math

import pytest


def find_pq(key_pair: RsaKeyPair):
    kphi = key_pair.d * key_pair.e - 1
    t = kphi

    while t % 2 == 0:
        t //= 2

    a = 2
    while a < 100:
        k = t
        while k < kphi:
            x = mod_power(a, k, key_pair.n)
            if x != 1 and x != key_pair.n - 1 and mod_power(x, 2, key_pair.n) == 1:
                p = math.gcd(x - 1, key_pair.n)
                break
            k *= 2
        a += 2
    q = key_pair.n // p

    return p, q


def rsa_attack(key_pair: RsaKeyPair, public_key: tuple[int, int]) -> RsaKeyPair:
    n = public_key[0]
    if n != key_pair.n:
        raise ValueError("Parameter `n` must be equal")

    p, q = find_pq(key_pair)
    totient = (p - 1) * (q - 1)

    e = public_key[1]
    d = mod_inverse(e, totient)

    return RsaKeyPair(n, d, e)


def test_rsa_attack_throw_when_n_not_equal():
    key_pair = RsaKeyPair(1, 2, 3)
    public_key = (4, 5)

    with pytest.raises(ValueError):
        _ = rsa_attack(key_pair, public_key)


def test_rsa_attack_succesfull():
    p, q = 53, 47

    key_pair_1 = rsa_keygen(p, q)
    key_pair_2 = key_pair_1
    while key_pair_2 == key_pair_1:
        key_pair_2 = rsa_keygen(p, q)

    key_pair_2_cracked = rsa_attack(key_pair_1, key_pair_2.public_key())
    assert key_pair_2_cracked == key_pair_2


if __name__ == "__main__":
    p, q = 5737, 6547

    key_pair_1 = rsa_keygen(p, q, e=23)
    print(f"{key_pair_1 = }")

    public_key_2 = (key_pair_1.n, 17)

    key_pair_2_cracked = rsa_attack(key_pair_1, public_key_2)
    print(f"{key_pair_2_cracked = }")

    original_message = 1234
    decrypted_message = key_pair_2_cracked.decrypt(key_pair_2_cracked.encrypt(original_message))
    print(f"{original_message = }")
    print(f"{decrypted_message = }")
