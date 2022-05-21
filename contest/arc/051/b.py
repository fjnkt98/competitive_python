from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    K: int = int(input())

    fibonacci: List[int] = [1] * 41
    for i in range(2, 41):
        fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]

    a = fibonacci[K - 1]
    b = fibonacci[K]
    print(a, b)


if __name__ == "__main__":
    main()
