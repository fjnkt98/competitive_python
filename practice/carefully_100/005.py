from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    A, B, C, X, Y = map(int, input().split())

    answer: int = A * X + B * Y
    for i in range(2 * max(X, Y) + 1):
        cost: int = i * C

        x: int = X - i // 2
        y: int = Y - i // 2

        if x > 0:
            cost += x * A
        if y > 0:
            cost += y * B

        answer = min(answer, cost)

    print(answer)


if __name__ == "__main__":
    main()
