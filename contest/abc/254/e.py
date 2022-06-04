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
    N, M = map(int, input().split())
    graph: List[List[int]] = [[] for i in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)

    Q: int = int(input())
    query: List[List[int]] = [list(map(int, input().split())) for i in range(Q)]

    distance: List[int] = [-1] * N

    for x, k in query:
        x -= 1

        candidate = collections.deque([x])
        history: List[int] = [x]
        distance[x] = 0
        D: int = 0

        while candidate:
            node = candidate.popleft()
            if distance[node] == k:
                continue

            for next_node in graph[node]:
                if distance[next_node] != -1:
                    continue
                distance[next_node] = distance[node] + 1
                history.append(next_node)
                candidate.append(next_node)

        answer: int = 0
        for h in history:
            answer += h + 1
            distance[h] = -1

        print(answer)


if __name__ == "__main__":
    main()
