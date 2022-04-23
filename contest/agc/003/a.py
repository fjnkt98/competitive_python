from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)


def main():
    S: str = input()

    count = collections.Counter(S)

    ok: bool = True
    if (count["N"] == 0 and count["S"] != 0) or (count["N"] != 0 and count["S"] == 0):
        ok = False
    if (count["W"] == 0 and count["E"] != 0) or (count["W"] != 0 and count["E"] == 0):
        ok = False

    print("Yes" if ok else "No")


if __name__ == "__main__":
    main()
