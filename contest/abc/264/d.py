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


sys.setrecursionlimit(1000000)


def main():
    S: str = input()
    D: Dict[str, int] = {
        "a": 0,
        "t": 1,
        "c": 2,
        "o": 3,
        "d": 4,
        "e": 5,
        "r": 6,
    }
    T: List[int] = [D[s] for s in S]

    answer: int = 0
    for i, j in itertools.combinations(range(7), r=2):
        if T[i] > T[j]:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
