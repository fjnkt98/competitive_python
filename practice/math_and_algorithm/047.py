from typing import List, Tuple, Deque
import sys
from array import array
import collections


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dfs(graph: List[List[int]], colors: List[int], node: int, color: int) -> bool:
    colors[node] = color

    for next_node in graph[node]:
        if colors[next_node] != -1:
            if colors[next_node] == color:
                return False

            continue

        if dfs(graph, colors, next_node, 1 - color) is False:
            return False

    return True


def main():
    N, M = map(int, input().split())
    graph: List[List[int]] = [[] for i in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        graph[A - 1].append(B - 1)
        graph[B - 1].append(A - 1)

    colors: List[int] = [-1 for i in range(N)]

    ok: bool = True
    for i in range(N):
        if colors[i] != -1:
            continue
        if dfs(graph, colors, i, 0) is False:
            ok = False

    print("Yes" if ok else "No")


if __name__ == "__main__":
    main()
