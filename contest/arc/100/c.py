from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))
    B: List[int] = [a - i - 1 for i, a in enumerate(A)]

    B.sort()
    b: int = B[N // 2] if N % 2 == 1 else (B[N // 2 - 1] + B[N // 2]) // 2

    print(sum(map(lambda x: abs(x - b), B)))


if __name__ == "__main__":
    main()
