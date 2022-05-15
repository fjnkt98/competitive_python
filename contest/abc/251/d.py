from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    W: int = int(input())

    answer: List[int] = (
        list(range(1, 100))
        + list(range(100, 9901, 100))
        + list(range(10000, 990001, 10000))
    )
    print(len(answer))
    print(*answer)


if __name__ == "__main__":
    main()
