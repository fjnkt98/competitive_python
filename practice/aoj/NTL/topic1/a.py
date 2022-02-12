from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def prime_factorize(N: int) -> List[Tuple[int, int]]:
    primes: List[Tuple[int, int]] = []

    i: int = 2
    while i * i <= N:
        if N % i == 0:
            exp: int = 0

            while N % i == 0:
                exp += 1
                N //= i

            primes.append((i, exp))

        i += 1

    if N != 1:
        primes.append((N, 1))

    return primes


def main():
    N: int = int(input())

    primes: List[Tuple[int, int]] = prime_factorize(N)

    result: List[int] = []
    for p, e in primes:
        for i in range(e):
            result.append(p)

    print("{}: {}".format(N, " ".join(map(str, result))))


if __name__ == "__main__":
    main()
