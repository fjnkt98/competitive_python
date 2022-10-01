from typing import *
import collections
import itertools
import bisect
import math


def main():
    H, W = map(int, input().split())
    S: List[List[str]] = [list(input()) for i in range(H)]

    for i, j in itertools.product(range(H), range(W)):
        if S[i][j] == "a":
            a = i, j
        if S[i][j] == "g":
            g = i, j
        if S[i][j] == "s":
            s = i, j

    D: List[List[List[List[int]]]] = [
        [[[-1 for l in range(W)] for k in range(H)] for j in range(W)] for i in range(H)
    ]
    sr, sc = s
    ar, ac = a
    D[sr][sc][ar][ac] = 0

    Q = collections.deque([(sr, sc, ar, ac)])

    DR: List[int] = [0, 1, 0, -1]
    DC: List[int] = [1, 0, -1, 0]
    while Q:
        sr, sc, ar, ac = Q.popleft()

        for dr, dc in zip(DR, DC):
            n_sr: int = sr + dr
            n_sc: int = sc + dc

            n_ar: int = (ar + dr) if (n_sr, n_sc) == (ar, ac) else ar
            n_ac: int = (ac + dc) if (n_sr, n_sc) == (ar, ac) else ac

            if (
                0 <= n_sr < H
                and 0 <= n_sc < W
                and 0 <= n_ar < H
                and 0 <= n_ac < W
                and S[n_sr][n_sc] != "#"
                and S[n_ar][n_ac] != "#"
                and D[n_sr][n_sc][n_ar][n_ac] == -1
            ):
                if (n_ar, n_ac) == g:
                    print(D[sr][sc][ar][ac] + 1)
                    return
                D[n_sr][n_sc][n_ar][n_ac] = D[sr][sc][ar][ac] + 1
                Q.append((n_sr, n_sc, n_ar, n_ac))

    print(-1)


if __name__ == "__main__":
    main()
