from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def f(M: int, N: int) -> int:
    return M * (N - M + 1) + 1


def main():
    N, K = map(int, input().split())
    mod: int = 1000000007

    answer: int = 0
    for k in range(K, N + 2):
        answer += f(k, N)
        answer %= mod

    print(answer)


if __name__ == "__main__":
    main()
