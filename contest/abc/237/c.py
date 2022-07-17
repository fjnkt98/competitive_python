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
    T: List[Tuple[str, int]] = [(k, len(list(v))) for k, v in itertools.groupby(S)]

    ok: bool = False
    if S == S[::-1]:
        ok = True
    else:
        B = T[0]
        E = T[-1]

        if B[0] == "a":
            if E[0] == "a":
                if E[1] - B[1] >= 0:
                    U: str = S.strip("a")
                    if U == U[::-1]:
                        ok = True
        else:
            if E[0] == "a":
                U: str = S.rstrip("a")
                if U == U[::-1]:
                    ok = True

    print("Yes" if ok else "No")


if __name__ == "__main__":
    main()
