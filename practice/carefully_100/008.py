from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A, B = zip(*[tuple(map(int, input().split())) for i in range(N)])

    C: List[int] = A + B
    answer: int = 1 << 60
    for s, t in itertools.product(C, repeat=2):
        distance: int = 0
        for a, b in zip(A, B):
            distance += abs(s - a) + abs(a - b) + abs(b - t)

        answer = min(answer, distance)

    print(answer)


if __name__ == "__main__":
    main()
