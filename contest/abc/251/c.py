from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools
import operator


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    posts: List[Tuple[str, str]] = [input().split() for i in range(N)]

    origin: Dict[str, Tuple[int, int]] = {}
    for i, (s, t) in enumerate(posts):
        p: int = int(t)

        if s not in origin:
            origin[s] = (i + 1, p)

    origin = list(origin.values())
    origin.sort(key=operator.itemgetter(1), reverse=True)
    print(origin[0][0])


if __name__ == "__main__":
    main()
