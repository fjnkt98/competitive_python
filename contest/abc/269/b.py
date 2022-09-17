from typing import *
import collections
import itertools
import bisect
import math


def main():
    S: List[str] = [input() for i in range(10)]

    X: List[int] = [i for i, s in enumerate(S) if s.count(".") != 10]
    A: int = X[0] + 1
    B: int = X[-1] + 1
    Y: List[int] = [i for i, c in enumerate(S[X[0]]) if c == "#"]
    C: int = Y[0] + 1
    D: int = Y[-1] + 1
    print(A, B)
    print(C, D)


if __name__ == "__main__":
    main()
