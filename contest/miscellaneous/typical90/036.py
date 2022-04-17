from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def distance(s: Tuple[int, int], t: Tuple[int, int]) -> int:
    return abs(s[0] - t[0]) + abs(s[1] - t[1])


def main():
    N, Q = map(int, input().split())
    P: List[Tuple[int, int]] = [tuple(map(int, input().split())) for i in range(N)]
    query: List[int] = [int(input()) for i in range(Q)]

    R: List[Tuple[int, int]] = [(x - y, x + y) for x, y in P]

    S: List[List[int]] = list(zip(*R))
    X: List[int] = S[0]
    Y: List[int] = S[1]

    Xmin: int = min(X)
    Xmax: int = max(X)
    Ymin: int = min(Y)
    Ymax: int = max(Y)

    for q in query:
        x, y = R[q - 1]

        print(max(abs(x - Xmin), abs(x - Xmax), abs(y - Ymin), abs(y - Ymax)))


if __name__ == "__main__":
    main()
