from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    while True:
        N, X = map(int, input().split())

        if N == 0 and X == 0:
            return

        answer: int = 0
        for i, j, k in itertools.combinations(list(range(1, N + 1)), 3):
            if i + j + k == X:
                answer += 1

        print(answer)


if __name__ == "__main__":
    main()
