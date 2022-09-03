from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    A: List[List[int]] = [list(map(int, input().split())) for i in range(N)]

    edges: List[List[int]] = sorted(
        [(A[i][j], i, j) for i, j in itertools.combinations(range(N), r=2)],
        reverse=True,
    )

    answer: int = sum(
        [A[i][j] for i, j in itertools.combinations(range(N), r=2)],
    )
    for w, a, b in edges:
        if A[a][b] == 1 << 60:
            continue

        for i in range(N):
            if i in [a, b] or A[a][i] == 1 << 60 or A[i][b] == 1 << 60:
                continue

            if A[a][i] + A[i][b] == w:
                answer -= w
                A[a][b] = A[b][a] = 1 << 60
                break
            elif A[a][i] + A[i][b] < w:
                print(-1)
                return

    print(answer)


if __name__ == "__main__":
    main()
