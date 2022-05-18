from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, C = map(int, input().split())
    A: List[int] = [int(input()) for i in range(N)]

    colors: List[int] = list(set(A))

    if len(colors) == 1:
        complement: Set[int] = {i + 1 for i in range(10)} - set(A)

        colors.append(complement.pop())

    answer: int = 1 << 60
    for c1, c2 in itertools.combinations(colors, 2):
        pattern1: List[int] = [c1 if i % 2 == 0 else c2 for i in range(N)]
        pattern2: List[int] = [c1 if i % 2 == 1 else c2 for i in range(N)]

        cost1: int = 0
        for a, p in zip(A, pattern1):
            if a != p:
                cost1 += C

        cost2: int = 0
        for a, p in zip(A, pattern2):
            if a != p:
                cost2 += C

        answer = min(answer, cost1, cost2)

    print(answer)


if __name__ == "__main__":
    main()
