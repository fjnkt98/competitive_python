from typing import List, Tuple, Set
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[List[int]] = [list(map(int, input().split())) for i in range(N)]
    M: int = int(input())
    XY: Set[Tuple[int, int]] = set()
    for i in [0] * M:
        X, Y = map(int, input().split())
        X -= 1
        Y -= 1
        XY.add((X, Y))
        XY.add((Y, X))

    answer: int = 1 << 60
    for P in itertools.permutations([i for i in range(N)]):
        total: int = 0
        for i, p in enumerate(P):
            total += A[p][i]

        ok: bool = True
        for i in range(N - 1):
            if (P[i], P[i + 1]) in XY:
                ok = False

        if ok:
            answer = min(answer, total)

    print(answer if answer != (1 << 60) else -1)


if __name__ == "__main__":
    main()
