from typing import List, Tuple
import sys
from array import array
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    C1: List[int] = [0 for i in range(N + 1)]
    C2: List[int] = [0 for i in range(N + 1)]
    for i in range(1, N + 1):
        c, p = map(int, input().split())

        if c == 1:
            C1[i] = p
        else:
            C2[i] = p

    cumsum1: List[int] = list(itertools.accumulate(C1))
    cumsum2: List[int] = list(itertools.accumulate(C2))

    Q: int = int(input())
    answer: List[List[int]] = [[] for i in range(Q)]
    for i in range(Q):
        l, r = map(int, input().split())

        answer[i] = (cumsum1[r] - cumsum1[l - 1], cumsum2[r] - cumsum2[l - 1])

    for a in answer:
        print(*a)


if __name__ == "__main__":
    main()
