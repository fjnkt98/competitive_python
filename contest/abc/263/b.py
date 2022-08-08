from typing import (
    List,
    Tuple,
    Deque,
    Set,
    Dict,
    TypeVar,
    Callable,
    Generic,
    Iterable,
    Iterator,
    Union,
)
import sys
import collections
import itertools
import bisect
import math


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    P: List[int] = list(map(lambda x: int(x) - 1, input().split()))
    graph: List[List[int]] = [[] for i in range(N)]
    for i, p in enumerate(P):
        graph[p].append(i + 1)

    D: List[int] = [-1 if i != 0 else 0 for i in range(N)]
    C = collections.deque([0])

    while C:
        node = C.popleft()

        for next_node in graph[node]:
            if D[next_node] == -1:
                D[next_node] = D[node] + 1
                C.append(next_node)

    print(D[N - 1])


if __name__ == "__main__":
    main()
