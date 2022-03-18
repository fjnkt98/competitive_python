from typing import List, Tuple
import sys
from array import array
import math


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def is_prime(N: int) -> bool:
    if N <= 1:
        return False
    if N == 2:
        return True

    i: int = 2
    while i * i <= N:
        if N % i == 0:
            return False

        i += 1

    return True


def main():
    L, R = map(int, input().split())

    N = int(math.sqrt(R) + 0.1)
    F1: List[bool] = [True for i in range(N + 1)]
    F2: List[bool] = [True for i in range(R - L + 1)]

    if L == 1:
        F2[0] = False

    for p in range(2, N + 1):
        if not F1[p]:
            continue

        q = p * 2
        while q * q <= R:
            F1[q] = False
            q += p

        start: int = L + (-L) % p
        if start == p:
            start = p * 2

        q = start
        while q <= R:
            F2[q - L] = False
            q += p

    print(F2.count(True))


if __name__ == "__main__":
    main()
