from typing import List
from sys import setrecursionlimit


setrecursionlimit(10000)


def dfs(
    G: List[List[int]],
    depth: List[int],
    current_node: int,
    previous_node: int,
    current_depth: int,
):
    for next_node in G[current_node]:
        if next_node == previous_node:
            continue
        depth[next_node] = current_depth + 1
        dfs(G, depth, next_node, current_node, current_depth + 1)


def main():
    N = int(input())
    P = list(map(int, input().split()))

    G: List[List[int]] = [[] for i in range(N)]
    for i, p in enumerate(P, 1):
        G[p].append(i)

    depth: List[int] = [0 for i in range(N)]

    dfs(G, depth, 0, -1, 0)

    for d in depth:
        print(d)


if __name__ == "__main__":
    main()
