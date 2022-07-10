from typing import (
    List,
    Tuple,
    Deque,
    Set,
    Dict,
    TypeVar,
    Callable,
    Generic,
    Iterable,
    Iterator,
    Union,
)
import sys
import collections
import itertools
import bisect
import math
import numpy as np


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    a, b, d = map(int, input().split())

    p = np.array([[a], [b]])
    rad = np.radians(d)
    R = np.array([[np.cos(rad), -np.sin(rad)], [np.sin(rad), np.cos(rad)]])

    q = np.dot(R, p)
    print(q[0, 0], q[1, 0])


if __name__ == "__main__":
    main()
