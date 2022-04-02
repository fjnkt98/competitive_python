from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


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
    N, P = map(int, input().split())

    primes: List[int] = factorize(P)

    candidate: List[int] = []
    for p in primes:
        exp: int = p[1]

        while exp >= N:
            candidate.append(p[0])
            exp -= N

    answer: int = 1
    for c in candidate:
        answer *= c

    print(answer)


if __name__ == "__main__":
    main()
