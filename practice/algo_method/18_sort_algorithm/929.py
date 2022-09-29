from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, X = map(int, input().split())
    S: List[str] = [""] * N
    H: List[int] = [0] * N
    for i in range(N):
        s, h = input().split()
        S[i] = s
        H[i] = int(h)

    T: List[Tuple[int, int, int]] = sorted(
        [(h, i, s) for i, (s, h) in enumerate(zip(S, H))]
    )

    index: int = -1
    for j, (h, i, s) in enumerate(T):
        if i == X:
            index = j

    print(T[index - 1][2])
    print(T[index + 1][2])


if __name__ == "__main__":
    main()
