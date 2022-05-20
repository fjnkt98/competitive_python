from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))
    Q: int = int(input())
    M: List[int] = list(map(int, input().split()))

    result: Set[int] = set()
    for bits in itertools.product((0, 1), repeat=N):
        total: int = 0
        for bit, a in zip(bits, A):
            if bit == 1:
                total += a

        result.add(total)

    for m in M:
        if m in result:
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    main()
