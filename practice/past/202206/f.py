from typing import *
import collections
import itertools
import bisect
import math


def main():
    H, W = map(int, input().split())
    S: List[List[int]] = [list(map(int, input().split())) for i in range(H)]
    N: int = int(input())
    R, C = map(
        list, zip(*[list(map(lambda x: int(x) - 1, input().split())) for i in range(N)])
    )

    for r, c in zip(R, C):
        if S[r][c] == 0:
            continue

        S[r][c] = 0
        if r > 0 and S[r - 1][c] != 0:
            while r > 0:
                S[r][c], S[r - 1][c] = S[r - 1][c], S[r][c]
                r -= 1

    for s in S:
        print(*s)


if __name__ == "__main__":
    main()
