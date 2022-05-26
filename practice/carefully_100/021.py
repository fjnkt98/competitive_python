from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    H, S = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    left: int = 0
    right: int = 1 << 60

    while right - left > 1:
        mid: int = (right + left) >> 1

        ok: bool = True
        time_limits: List[int] = sorted([(mid - h) // s for h, s in zip(H, S)])

        time: int = 0
        for t in time_limits:
            if time <= t:
                time += 1
            else:
                ok = False

        if ok:
            right = mid
        else:
            left = mid

    print(right)


if __name__ == "__main__":
    main()
