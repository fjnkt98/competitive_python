from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    P: List[int] = [tuple(map(int, input().split())) for i in range(N)]

    X: List[Set[int]] = [set() for i in range(5001)]
    Y: List[Set[int]] = [set() for i in range(5001)]
    for x, y in P:
        X[x].add(y)
        Y[y].add(x)

    answer: int = 0
    for (x1, y1), (x2, y2) in itertools.combinations(P, 2):
        x_diff: int = abs(x1 - x2)
        y_diff: int = abs(y1 - y2)

        x3: int = x2 + y_diff
        y3: int = y2 + x_diff
        x4: int = x1 + y_diff
        y4: int = y1 + x_diff

        if (
            0 <= x3 <= 5000
            and 0 <= y3 <= 5000
            and 0 <= x4 <= 5000
            and 0 <= y4 <= 5000
            and y3 in X[x3]
            and y4 in X[x4]
        ):
            answer = max(answer, x_diff ** 2 + y_diff ** 2)

        x3 = x2 - y_diff
        y3 = y2 - x_diff
        x4 = x1 - y_diff
        y4 = y1 - x_diff

        if (
            0 <= x3 <= 5000
            and 0 <= y3 <= 5000
            and 0 <= x4 <= 5000
            and 0 <= y4 <= 5000
            and y3 in X[x3]
            and y4 in X[x4]
        ):
            answer = max(answer, x_diff ** 2 + y_diff ** 2)

    print(answer)


if __name__ == "__main__":
    main()
