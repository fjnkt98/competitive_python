from typing import List
import sys


sys.setrecursionlimit(10000)
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
    N: int = int(input())

    for i in range(N, 0, -1):
        if is_prime(i):
            print(i)
            break


if __name__ == "__main__":
    main()
