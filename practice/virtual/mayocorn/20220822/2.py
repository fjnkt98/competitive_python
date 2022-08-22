from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())

    count: int = 0
    S: Set[int] = set()
    for a in range(2, 100001):
        for b in range(2, math.ceil(math.log(N, a)) + 2):
            ab: int = pow(a, b)
            if ab <= N and ab not in S:
                count += 1
                S.add(ab)

    print(N - count)


if __name__ == "__main__":
    main()
