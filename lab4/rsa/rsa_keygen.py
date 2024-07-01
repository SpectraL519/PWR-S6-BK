from utility import is_prime, mod_inverse
from rsa_key_pair import RsaKeyPair

import math
import random

import pytest


def rsa_keygen(p: int, q: int, e: int = None) -> RsaKeyPair:
    if p == q:
        raise ValueError("Parameters `p` and `q` cannot be equal")

    if not is_prime(p):
        raise ValueError("Parameter `p` must be a prime number")

    if not is_prime(q):
        raise ValueError("Parameter `q` must be a prime number")

    n = p * q
    totient = (p - 1) * (q - 1)

    # select public key: e
    if e is None:
        found_e = False
        while not found_e:
            e = random.randint(2, totient - 1)
            found_e = math.gcd(e, totient) == 1

    # select private key: d
    d = mod_inverse(e, totient)

    return RsaKeyPair(n, d, e)


def test_rsa_keygen_throw_when_p_and_q_are_equal():
    with pytest.raises(ValueError):
        _ = rsa_keygen(13, 13)


def test_rsa_keygen_throw_when_p_not_prime():
    with pytest.raises(ValueError):
        _ = rsa_keygen(12, 13)


def test_rsa_keygen_throw_when_q_not_prime():
    with pytest.raises(ValueError):
        _ = rsa_keygen(13, 12)


def test_rsa_keygen_correct_message_encryption_and_decryption():
    p, q = 53, 47

    key_pair = rsa_keygen(p, q)
    message = 1234

    assert key_pair.decrypt(key_pair.encrypt(message)) == message
