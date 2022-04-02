from typing import List, Tuple, Set
import sys
import collections
import itertools
import bisect


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    X, N = map(int, input().split())
    P: List[int] = list(map(int, input().split()))

    C: List[int] = sorted(list(set(range(-1, 102)) - set(P)))
    answer: int = 0
    minimum_diff: int = 10000
    for c in reversed(C):
        if abs(X - c) <= minimum_diff:
            answer = c
            minimum_diff = abs(X - c)

    print(answer)


if __name__ == "__main__":
    main()
