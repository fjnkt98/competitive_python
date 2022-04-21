from typing import List, Tuple
import sys
import collections
import itertools
import numpy as np
import math
import functools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, X = map(int, input().split())
    P: List[int] = list(map(int, input().split()))

    P.append(X)

    diff: List[int] = np.diff(np.array(sorted(P))).tolist()

    answer: int = functools.reduce(math.gcd, diff)
    print(answer)


if __name__ == "__main__":
    main()
