from typing import List
from sys import setrecursionlimit


setrecursionlimit(10000)


def dfs(G: List[List[int]], colored: List[int], current_node: int, previous_node: int):
    colored.append(current_node)

    for next_node in G[current_node]:
        if next_node == previous_node:
            continue
        dfs(G, colored, next_node, current_node)


def main():
    N = int(input())
    P = list(map(int, input().split()))

    G: List[List[int]] = [[] for i in range(N)]
    for i, p in enumerate(P, 1):
        G[p].append(i)

    for g in G:
        g.sort()

    answer: List[int] = []
    dfs(G, answer, 0, -1)

    print(" ".join(map(str, answer)))


if __name__ == "__main__":
    main()
