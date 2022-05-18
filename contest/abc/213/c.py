from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def compress(A: List[int]) -> List[int]:
    X: List[int] = sorted(set(A))
    D: Dict[int, int] = {x: i for i, x in enumerate(X)}
    return list(map(lambda x: D[x], A))


def main():
    H, W, N = map(int, input().split())
    A: List[int] = [0] * N
    B: List[int] = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    for a, b in zip(compress(A), compress(B)):
        print(a + 1, b + 1)


if __name__ == "__main__":
    main()
