from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
# input = sys.stdin.readline


def convert_from_8_to_9(N: str) -> str:
    decimal: int = 0
    digit = 1
    for c in reversed(N):
        decimal += int(c) * digit
        digit *= 8

    result: List[int] = []
    while decimal:
        result.append(decimal % 9)
        decimal //= 9

    return "".join(map(str, reversed(result)))


def convert_from_9_to_8(N: str) -> str:
    decimal: int = 0
    digit = 1
    for c in reversed(N):
        decimal += int(c) * digit
        digit *= 9

    result: List[int] = []
    while decimal:
        result.append(decimal % 8)
        decimal //= 8

    return "".join(map(str, reversed(result)))


def main():
    N, K = input().split()
    K = int(K)

    if N == "0":
        print(0)
        return

    for i in [0] * K:
        N = convert_from_8_to_9(N)
        N = N.replace("8", "5")

    print(N)


if __name__ == "__main__":
    main()
