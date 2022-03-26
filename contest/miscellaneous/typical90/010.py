from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    CP: List[List[int]] = [list(map(int, input().split())) for i in range(N)]
    Q: int = int(input())
    LR: List[List[int]] = [list(map(int, input().split())) for i in range(Q)]

    P1: List[int] = [0] * N
    P2: List[int] = [0] * N
    for i, cp in enumerate(CP):
        c, p = cp
        if c == 1:
            P1[i] = p
        else:
            P2[i] = p

    cumsum1: List[int] = list(itertools.accumulate(P1))
    cumsum2: List[int] = list(itertools.accumulate(P2))
    cumsum1.insert(0, 0)
    cumsum2.insert(0, 0)

    for l, r in LR:
        print(cumsum1[r] - cumsum1[l - 1], cumsum2[r] - cumsum2[l - 1])


if __name__ == "__main__":
    main()
