from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())

    grid: List[List[bool]] = [[True] * W for i in range(H)]

    dr: List[int] = [0, 1, 0, -1]
    dc: List[int] = [1, 0, -1, 0]

    answer: int = 0
    for i in range(4):
        nr = R + dr[i] - 1
        nc = C + dc[i] - 1

        if 0 <= nr < H and 0 <= nc < W:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
