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
import re


sys.setrecursionlimit(1000000)


def main():
    N: int = int(input())
    S: str = input()

    G: List[str] = re.findall(r"A+RC+", S)
    X: List[int] = [min(b.count("A"), b.count("C")) for b in G]
    print(min(sum(X), 2 * len(G)))


if __name__ == "__main__":
    main()
