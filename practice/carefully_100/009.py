from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    M: int = int(input())
    pattern: List[Tuple[int, int]] = [
        tuple(map(int, input().split())) for i in range(M)
    ]
    N: int = int(input())
    picture: List[Tuple[int, int]] = [
        tuple(map(int, input().split())) for i in range(N)
    ]

    D: Dict[int, Set[int]] = collections.defaultdict(set)
    for x, y in picture:
        D[x].add(y)

    for xp, yp in picture:
        x0, y0 = pattern[0]
        x_diff: int = xp - x0
        y_diff: int = yp - y0

        moved_pattern: List[int] = [(x + x_diff, y + y_diff) for x, y in pattern]

        match: bool = True
        for x, y in moved_pattern:
            if y not in D[x]:
                match = False

        if match:
            print(x_diff, y_diff)
            return


if __name__ == "__main__":
    main()
