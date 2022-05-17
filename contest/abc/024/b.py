from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, T = map(int, input().split())
    A: List[int] = [int(input()) for i in range(N)]

    B: List[int] = [0] * (2 * 1000000)
    for a in A:
        B[a] += 1
        B[a + T] -= 1

    C: List[int] = list(itertools.accumulate(B))
    answer: int = 0
    for c in C:
        if c > 0:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
