from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    graph: List[List[int]] = [[] for i in range(N)]
    for i, a in enumerate(map(lambda x: x - 1, A)):
        graph[a].append(i + 1)

    answer: List[int] = [len(node) for node in graph]
    for a in answer:
        print(a)


if __name__ == "__main__":
    main()
