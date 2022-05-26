from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools
import bisect


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    L: int = int(input())
    N: int = int(input())
    M: int = int(input())
    D: List[int] = [0] + list(sorted([int(input()) for i in range(N - 1)])) + [L]
    K: List[int] = [int(input()) for i in range(M)]

    answer: int = 0
    for k in K:
        i: int = bisect.bisect_left(D, k)
        answer += min(abs(D[i] - k), abs(k - D[i - 1]))

    print(answer)


if __name__ == "__main__":
    main()
