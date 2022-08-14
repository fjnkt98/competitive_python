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


def f(A: List[List[str]]) -> int:
    I: int = 0
    B: List[List[int]] = [[-1] * 10 for i in range(10)]
    for i, j in itertools.product(range(10), repeat=2):
        if A[i][j] == "x" or B[i][j] != -1:
            continue
        I += 1
        candidate = collections.deque([(i, j)])
        while candidate:
            r, c = candidate.popleft()

            for dr, dc in zip([0, 1, 0, -1], [1, 0, -1, 0]):
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < 10
                    and 0 <= nc < 10
                    and A[nr][nc] == "o"
                    and B[nr][nc] == -1
                ):
                    candidate.append((nr, nc))
                    B[nr][nc] = I

    return I


def main():
    A: List[List[str]] = [list(input()) for i in range(10)]

    if f(A) == 1:
        print("YES")
        return

    for i, j in itertools.product(range(10), repeat=2):
        if A[i][j] == "o":
            continue
        A[i][j] = "o"

        if f(A) == 1:
            print("YES")
            return
        A[i][j] = "x"

    print("NO")


if __name__ == "__main__":
    main()
