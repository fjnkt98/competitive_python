from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    T: int = int(input())
    C: List[List[int]] = [sorted(tuple(map(int, input().split()))) for i in range(T)]

    for r, g, b in C:
        answer: int = 1 << 60
        if g % 3 == b % 3:
            answer = min(answer, b)
        if r % 3 == b % 3:
            answer = min(answer, b)
        if r % 3 == g % 3:
            answer = min(answer, g)

        if answer == 1 << 60:
            print(-1)
        else:
            print(answer)


if __name__ == "__main__":
    main()
