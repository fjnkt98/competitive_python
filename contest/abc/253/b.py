from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)


def main():
    H, W = map(int, input().split())
    grid: List[str] = [input() for i in range(H)]

    P: List[Tuple[int, int]] = []

    for i, j in itertools.product(range(H), range(W)):
        if grid[i][j] == "o":
            P.append((i, j))

    si, sj = P[0]
    ti, tj = P[1]

    answer: int = abs(si - ti) + abs(sj - tj)
    print(answer)


if __name__ == "__main__":
    main()
