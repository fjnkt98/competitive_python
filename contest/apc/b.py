from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))
    B: List[int] = list(map(int, input().split()))

    operations: int = sum(B) - sum(A)
    if operations == 0:
        print("Yes" if tuple(A) == tuple(B) else "No")
        return

    if operations < 0:
        print("No")
        return

    count: int = 0
    for i, (a, b) in enumerate(zip(A, B)):
        if a < b:
            count += (b - a + 1) // 2

    if count > operations:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
