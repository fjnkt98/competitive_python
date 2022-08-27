from typing import *
import collections
import itertools
import bisect
import math


import sys

sys.setrecursionlimit(1000000)


def dfs(S: str, A: List[int]):
    if len(S) == 10:
        return

    C = collections.Counter(S)
    if C["7"] >= 1 and C["5"] >= 1 and C["3"] >= 1:
        A.append(int(S))

    for c in ["7", "5", "3"]:
        dfs(S + c, A)


def main():
    N: int = int(input())

    A: List[int] = []
    for c in ["7", "5", "3"]:
        dfs(c, A)

    answer: List[int] = list(filter(lambda x: x <= N, A))
    print(len(answer))


if __name__ == "__main__":
    main()
