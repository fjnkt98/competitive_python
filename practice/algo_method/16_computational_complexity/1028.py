from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, D = map(int, input().split())
    X: List[int] = list(map(int, input().split()))

    C: List[int] = [0] + list(itertools.accumulate(X))

    count: int = 0
    l: int = -1
    for i in range(N - D + 1):
        if count <= C[i + D] - C[i]:
            count = C[i + D] - C[i]
            l = i

    print("{}~{}".format(l, l + D - 1))


if __name__ == "__main__":
    main()
