from typing import List, Tuple
import sys
from array import array


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
    N = int(input())

    print("Yes" if is_prime(N) else "No")


if __name__ == "__main__":
    main()
