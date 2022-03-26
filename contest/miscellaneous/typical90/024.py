from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    B: List[int] = list(map(int, input().split()))

    diff: int = 0
    for a, b in zip(A, B):
        diff += abs(a - b)

    if diff > K:
        print("No")
    else:
        if (K - diff) % 2 == 0:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
