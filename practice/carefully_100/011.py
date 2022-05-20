from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    S: List[List[int]] = [[] for i in range(M)]
    K: List[int] = [0 for i in range(M)]
    for i in range(M):
        k, *s = map(int, input().split())
        K[i] = k
        S[i] = s.copy()
    P: List[int] = list(map(int, input().split()))

    answer: int = 0
    for bits in itertools.product((0, 1), repeat=N):
        lit_all: bool = True
        for i, s in enumerate(S):
            total: int = 0
            for j in s:
                if bits[j - 1] == 1:
                    total += 1

            if total % 2 != P[i]:
                lit_all = False

        if lit_all:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
