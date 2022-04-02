from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def f(S: List[str], T: List[str]) -> int:
    distance: int = 0

    for s, t in zip(S, T):
        if s != t:
            distance += 1

    return distance


def main():
    S: str = input().rstrip()

    T1: List[str] = ["0" if i % 2 == 0 else "1" for i in range(len(S))]
    T2: List[str] = ["0" if i % 2 == 1 else "1" for i in range(len(S))]

    print(min(f(list(S), T1), f(list(S), T2)))


if __name__ == "__main__":
    main()
