from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools
import bisect


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(sorted(map(int, input().split())))
    B: List[int] = list(sorted(map(int, input().split())))
    C: List[int] = list(sorted(map(int, input().split())))

    answer: int = 0
    for b in B:
        i: int = bisect.bisect_left(A, b)
        j: int = bisect.bisect_right(C, b)

        answer += i * (N - j)

    print(answer)


if __name__ == "__main__":
    main()
