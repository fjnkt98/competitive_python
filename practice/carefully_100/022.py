from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools
import math


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def f(x: float, P: float) -> float:
    return 1 - P * math.log(2) * math.pow(2, -x / 1.5) / 1.5


def main():
    P: float = float(input())

    left: float = 0.0
    right: float = P

    while right - left > 1e-10:
        mid: float = (right + left) / 2

        if f(mid, P) < 0:
            left = mid
        else:
            right = mid

    answer: float = left + P / math.pow(2, left / 1.5)
    print("{:.8f}".format(answer))


if __name__ == "__main__":
    main()
