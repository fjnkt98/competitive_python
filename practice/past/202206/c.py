from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M = map(int, input().split())

    S: List[str] = []
    i: int = 1
    while i <= M:
        if i * math.log10(N) <= 9:
            S.append("o")
        else:
            S.append("x")
        i += 1

    print("".join(S))


if __name__ == "__main__":
    main()
