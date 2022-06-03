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


def main():
    S: str = input().rstrip()

    ok: bool = False

    for T in itertools.permutations("abc"):
        if S == "".join(T):
            ok = True

    print("Yes" if ok else "No")


if __name__ == "__main__":
    main()
