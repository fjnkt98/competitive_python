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
input = sys.stdin.readline


def solve(D: List[int]) -> str:
    current: List[Tuple[str, int]] = [("", 0)]

    for i, d in enumerate(D):
        next_position: List[Tuple[str, int]] = []
        while current:
            log, position = current.pop()

            if position + d <= 500:
                next_position.append((log + "R", position + d))
            if position - d >= -500:
                next_position.append((log + "L", position - d))

        history: Set[int] = set()
        for log, position in next_position:
            if position in history:
                continue
            else:
                history.add(position)
                current.append((log, position))

    log, _ = current[0]

    return log


def main():
    D: List[int] = list(map(int, input().split()))
    log = solve(D)

    history: List[int] = []
    p: int = 0
    for a, d in zip(log, D):
        if a == "R":
            p += d
        else:
            p -= d

        history.append(p)

    print(log, history)


if __name__ == "__main__":
    main()
