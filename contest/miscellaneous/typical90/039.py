from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dfs(graph: List[List[int]], dp: List[int], current: int, previous: int) -> None:
    dp[current] = 1

    for next_node in graph[current]:
        if next_node == previous:
            continue

        dfs(graph, dp, next_node, current)
        dp[current] += dp[next_node]


def main():
    N: int = int(input())
    graph: List[List[int]] = [[] for i in range(N)]
    for i in range(N - 1):
        a, b = map(int, input().split())

        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    dp: List[int] = [0] * N
    dfs(graph, dp, 0, -1)

    answer: int = 0
    for d in dp:
        answer += (N - d) * d

    print(answer)


if __name__ == "__main__":
    main()
