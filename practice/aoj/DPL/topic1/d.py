from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools
import bisect


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = [int(input()) for i in range(N)]

    dp: List[int] = [1 << 60] * N
    for i, a in enumerate(A):
        index = bisect.bisect_left(dp, a)
        dp[index] = a

    print(bisect.bisect_left(dp, 1 << 60))


if __name__ == "__main__":
    main()
