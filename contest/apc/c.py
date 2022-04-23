from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)


def main():
    N: int = int(input())

    left: int = 0
    right: int = N - 1

    print(0, flush=True)
    first: str = input()

    if first == "Vacant":
        return

    while right - left > 1:
        mid: int = (right + left) // 2

        print(mid, flush=True)
        s: str = input()

        if s == "Vacant":
            return

        if mid % 2 == 0:
            if first == s:
                left = mid
            else:
                right = mid
        else:
            if first != s:
                left = mid
            else:
                right = mid

    print(right, flush=True)
    if input() == "Vacant":
        return


if __name__ == "__main__":
    main()
