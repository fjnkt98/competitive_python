from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, K = map(int, input().split())
    P: List[List[int]] = [list(map(int, input().split())) for i in range(N)]

    Q: List[int] = sorted([sum(p) for p in P])
    for p in P:
        index: int = bisect.bisect_right(Q, sum(p) + 300)
        print("Yes" if N - index + 1 <= K else "No")


if __name__ == "__main__":
    main()
