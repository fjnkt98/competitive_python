from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools
import math

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    P: List[Tuple[int, int]] = [tuple(map(int, input().split())) for i in range(N)]

    def f(x1: int, y1: int, x2: int, y2: int) -> float:
        return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

    result: List[float] = []
    M: int = 0
    for p in itertools.permutations(P):
        M += 1
        distance: float = 0.0
        for (x1, y1), (x2, y2) in zip(p[:-1], p[1:]):
            distance += f(x1, y1, x2, y2)
        result.append(distance)

    print(sum(list(map(lambda x: x / M, result))))


if __name__ == "__main__":
    main()
