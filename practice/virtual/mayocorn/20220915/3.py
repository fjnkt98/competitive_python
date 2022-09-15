from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    S: List[List[str]] = [list(input()) for i in range(N)]

    ok: bool = False
    for i, j in itertools.product(range(N), repeat=2):
        white: int = 0
        black: int = 0
        for k in range(6):
            if j + k >= N:
                break
            if S[i][j + k] == ".":
                white += 1
            else:
                black += 1

        if white + black == 6 and white <= 2:
            ok = True

        white = 0
        black = 0
        for k in range(6):
            if i + k >= N:
                break
            if S[i + k][j] == ".":
                white += 1
            else:
                black += 1

        if white + black == 6 and white <= 2:
            ok = True

        white = 0
        black = 0
        for k in range(6):
            if i + k >= N or j + k >= N:
                break
            if S[i + k][j + k] == ".":
                white += 1
            else:
                black += 1

        if white + black == 6 and white <= 2:
            ok = True

        white = 0
        black = 0
        for k in range(6):
            if i + k >= N or j - k < 0:
                break
            if S[i + k][j - k] == ".":
                white += 1
            else:
                black += 1

        if white + black == 6 and white <= 2:
            ok = True

    print("Yes" if ok else "No")


if __name__ == "__main__":
    main()
