from typing import *
import collections
import itertools
import bisect
import math


def main():
    H, W, N, M = map(int, input().split())
    L: List[Tuple[int, int]] = [
        tuple(map(lambda x: int(x) - 1, input().split())) for i in range(N)
    ]
    B: List[Tuple[int, int]] = [
        tuple(map(lambda x: int(x) - 1, input().split())) for i in range(M)
    ]

    G1: List[List[str]] = [["." for j in range(W)] for i in range(H)]
    G2: List[List[str]] = [["." for j in range(W)] for i in range(H)]
    for a, b in L:
        G1[a][b] = "L"
        G2[a][b] = "L"

    for c, d in B:
        G1[c][d] = "#"
        G2[c][d] = "#"

    for r, c in L:
        nr: int = r + 1
        while nr < H and G1[nr][c] == ".":
            G1[nr][c] = "o"
            nr += 1
        nr = r - 1
        while 0 <= nr and G1[nr][c] == ".":
            G1[nr][c] = "o"
            nr -= 1

    for r, c in L:
        nc: int = c + 1
        while nc < W and G2[r][nc] == ".":
            G2[r][nc] = "o"
            nc += 1
        nc = c - 1
        while 0 <= nc and G2[r][nc] == ".":
            G2[r][nc] = "o"
            nc -= 1

    answer: int = 0
    for i, j in itertools.product(range(H), range(W)):
        if G1[i][j] in ["o", "L"] or G2[i][j] in ["o", "L"]:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
