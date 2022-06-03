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
    A: str = list(input())
    B: str = list(input())
    C: str = list(input())

    P: Dict[str, List[str]] = {
        "a": list(reversed(A)),
        "b": list(reversed(B)),
        "c": list(reversed(C)),
    }

    turn: str = "a"
    while True:
        if not P[turn]:
            print(turn.upper())
            return

        turn = P[turn].pop()


if __name__ == "__main__":
    main()
