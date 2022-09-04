from typing import *
import collections
import itertools
import bisect
import math


def factorize(N: int) -> List[Tuple[int, int]]:
    result: List[Tuple[int, int]] = []

    i: int = 2
    while i * i <= N:
        if N % i == 0:
            exp: int = 0

            while N % i == 0:
                N //= i
                exp += 1

            result.append((i, exp))
        i += 1

    if N != 1:
        result.append((N, 1))

    return result


def main():
    N: int = int(input())
    primes: List[Tuple[int, int]] = [[p] * e for p, e in factorize(N)]
    print(f"{N}:", *list(itertools.chain(*primes)))


if __name__ == "__main__":
    main()
