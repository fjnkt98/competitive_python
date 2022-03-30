from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dfs(graph: List[List[int]], colors: List[int], node: int, color: int) -> None:
    colors[node] = color

    for next_node in graph[node]:
        if colors[next_node] == -1:
            dfs(graph, colors, next_node, 1 - color)


def main():
    N: int = int(input())
    graph: List[List[int]] = [[] for i in range(N)]
    for i in range(N - 1):
        A, B = map(int, input().split())
        graph[A - 1].append(B - 1)
        graph[B - 1].append(A - 1)

    colors: List[int] = [0 if i == 0 else -1 for i in range(N)]
    dfs(graph, colors, 0, 0)

    answer: List[int] = []
    color: int = 0 if colors.count(0) >= N // 2 else 1
    for i, c in enumerate(colors):
        if c == color:
            answer.append(i + 1)

    print(*answer[: N // 2])


if __name__ == "__main__":
    main()
