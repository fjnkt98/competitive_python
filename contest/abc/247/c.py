from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def f(N: int, S: List[str]) -> List[str]:
    if N == 0:
        return [""]

    Sp: List[str] = f(N - 1, [str(N - 1)])
    return Sp + S + Sp


def main():
    N: int = int(input())

    print(*list(filter(lambda s: s != "", f(N, [str(N)]))))


if __name__ == "__main__":
    main()
