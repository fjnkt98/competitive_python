from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    S: List[str] = []
    P: List[str] = []
    for i in range(N):
        s, p = input().split()
        S.append(s)
        P.append(int(p))

    R: List[Tuple[int, int, int]] = sorted(
        [(s, -p, i) for i, (s, p) in enumerate(zip(S, P))]
    )

    answer: List[int] = [i for s, p, i in R]
    for a in answer:
        print(a + 1)


if __name__ == "__main__":
    main()
