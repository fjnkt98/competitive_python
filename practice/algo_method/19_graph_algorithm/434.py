from typing import List
from sys import setrecursionlimit


setrecursionlimit(10000)


def dfs(
    G: List[List[int]],
    descendants: List[int],
    current_node: int,
    previous_node: int,
):
    for next_node in G[current_node]:
        if next_node == previous_node:
            continue
        dfs(G, descendants, next_node, current_node)
        descendants[current_node] += descendants[next_node] + 1


def main():
    N = int(input())
    P = list(map(int, input().split()))

    G: List[List[int]] = [[] for i in range(N)]
    for i, p in enumerate(P, 1):
        G[p].append(i)

    descendants: List[int] = [0 for i in range(N)]
    dfs(G, descendants, 0, -1)

    for d in descendants:
        print(d)


if __name__ == "__main__":
    main()
