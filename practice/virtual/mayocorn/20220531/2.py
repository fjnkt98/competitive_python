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

    ok: bool = True

    if S[0] != "A":
        ok = False

    if S[2:-1].count("C") != 1:
        ok = False

    for k, v in collections.Counter(S).items():
        if k.isupper():
            if k == "A" or k == "C":
                continue
            ok = False

    print("AC" if ok else "WA")


if __name__ == "__main__":
    main()
