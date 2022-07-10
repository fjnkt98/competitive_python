from typing import (
    List,
    Tuple,
    Deque,
    Set,
    Dict,
    TypeVar,
    Callable,
    Generic,
    Iterable,
    Iterator,
    Union,
)
import sys
import collections
import itertools
import bisect
import math


sys.setrecursionlimit(1000000)


def main():
    N: int = int(input())
    S = [input() for i in range(N)]

    ok: bool = False
    for i, j in itertools.product(range(N), repeat=2):
        for dr, dc in [(0, 1), (1, 0), (1, 1), (1, -1)]:
            r: int = i
            c: int = j

            white: int = 0
            black: int = 0
            for k in range(6):
                if 0 <= r < N and 0 <= c < N:
                    if S[r][c] == "#":
                        black += 1
                    else:
                        white += 1
                else:
                    break

                r = r + dr
                c = c + dc

            if black + white == 6 and black >= 4:
                ok = True

    print("Yes" if ok else "No")


if __name__ == "__main__":
    main()
