from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    A, B = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    C: List[int] = [0 for i in range(max(*A, *B) + 2)]
    for a, b in zip(A, B):
        C[a] += 1
        C[b + 1] -= 1

    C = list(itertools.accumulate(C))
    print(max(C))


if __name__ == "__main__":
    main()
