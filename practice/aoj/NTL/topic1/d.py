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

    answer = N
    for p, e in primes:
        answer *= p - 1
        answer //= p

    print(answer)


if __name__ == "__main__":
    main()
