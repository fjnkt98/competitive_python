from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    A: List[List[int]] = [list(map(int, input().split())) for i in range(N)]

    answer: int = 0
    for i, j in itertools.combinations(range(M), 2):
        score: int = 0
        for a in A:
            score += max(a[i], a[j])

        answer = max(answer, score)

    print(answer)


if __name__ == "__main__":
    main()
