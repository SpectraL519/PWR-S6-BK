import math


def is_prime(n: int) -> bool:
    return (
        isinstance(n, int) and
        n > 1 and
        all(n % i for i in range(2, math.isqrt(n) + 1))
    )


def mod_inverse(x: int, p: int):
    return pow(x, -1, p)


def mod_power(x: int, exp: int, p: int) -> int:
    return pow(x, exp, p)
