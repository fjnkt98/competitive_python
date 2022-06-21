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
    X: List[int] = list(map(int, input().split()))
    C: List[int] = list(map(int, input().split()))

    graph: List[List[Tuple[int, int]]] = [[] for i in range(N)]
    indegree: List[int] = [0] * N
    for i, (x, c) in enumerate(zip(X, C)):
        graph[i].append((x - 1, c))
        indegree[x - 1] += 1

    heap = collections.deque([])
    for i, d in enumerate(indegree):
        if d == 0:
            heap.append(i)

    while heap:
        node = heap.popleft()

        for next_node, weight in graph[node]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                heap.append(next_node)

    answer: int = 0
    for node, degree in enumerate(indegree):
        if degree == 0:
            continue

        history: Set[int] = set()
        while node not in history:
            history.add(node)
            node = graph[node][0][0]

        answer += min([graph[node][0][1] for node in history])
        for h in history:
            indegree[h] -= 1

    print(answer)


if __name__ == "__main__":
    main()
