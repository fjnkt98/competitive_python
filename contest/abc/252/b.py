from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    B: List[int] = list(map(int, input().split()))

    dislike: List[bool] = [False] * N
    for b in B:
        dislike[b - 1] = True

    maximum: int = max(A)
    ok: bool = False
    for a, d in zip(A, dislike):
        if a == maximum and d:
            ok = True

    print("Yes" if ok else "No")


if __name__ == "__main__":
    main()
