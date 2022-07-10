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
    S = input()
    T = input()

    U: List[Tuple[str, int]] = [(k, len(list(v))) for k, v in itertools.groupby(S)]
    V: List[Tuple[str, int]] = [(k, len(list(v))) for k, v in itertools.groupby(T)]

    ok: bool = True

    if len(U) != len(V):
        print("No")
        return

    for u, v in zip(U, V):
        if u[0] != v[0]:
            ok = False
        elif (u[1] == 1 and v[1] != 1) or (u[1] > v[1]):
            ok = False

    print("Yes" if ok else "No")


if __name__ == "__main__":
    main()
