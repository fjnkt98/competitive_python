from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, D, K = map(int, input().split())
    L: List[int] = [0] * D
    R: List[int] = [0] * D
    for i in range(D):
        L[i], R[i] = map(int, input().split())

    S: List[int] = [0] * K
    T: List[int] = [0] * K
    for i in range(K):
        S[i], T[i] = map(int, input().split())

    answer: List[int] = [1 << 60] * K
    for i, (s, t) in enumerate(zip(S, T)):
        if s < t:
            for j, (l, r) in enumerate(zip(L, R)):
                if not (l <= s <= r):
                    continue
                if s < r:
                    s = r

                if t <= s:
                    answer[i] = j + 1
                    break
        else:
            for j, (l, r) in enumerate(zip(L, R)):
                if not (l <= s <= r):
                    continue
                if l < s:
                    s = l
                if s <= t:
                    answer[i] = j + 1
                    break

    for a in answer:
        print(a)


if __name__ == "__main__":
    main()
