from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, M, K = map(int, input().split())

    if N == 1 or M == 1:
        print("Yes")
        return

    ok: bool = False
    for i in range(N + 1):
        for j in range(M + 1):
            black: int = i * (M - j) + j * (N - i)

            if black == K:
                ok = True

    print("Yes" if ok else "No")


if __name__ == "__main__":
    main()
