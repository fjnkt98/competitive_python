from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools
import bisect


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, W = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    good: List[int] = A[:]
    for a, b in itertools.combinations(A, 2):
        good.append(a + b)

    for a, b, c in itertools.combinations(A, 3):
        good.append(a + b + c)

    good = sorted(list(set(good)))
    print(len(good[: bisect.bisect_right(good, W)]))


if __name__ == "__main__":
    main()
