from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    answer: int = N * (N - 1) * (N - 2) // 6
    count = collections.Counter(A)
    x: int = 0
    y: int = 0
    for k, v in count.items():
        x += (N - v) * (v * (v - 1) // 2)
        y += v * (v - 1) * (v - 2) // 6

    print(answer - x - y)


if __name__ == "__main__":
    main()
