from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dfs(
    graph: List[List[int]], dp: List[int], current_node: int, previous_node: int
) -> None:
    dp[current_node] = 1

    for next_node in graph[current_node]:
        if next_node == previous_node:
            continue
        dfs(graph, dp, next_node, current_node)
        dp[current_node] += dp[next_node]


def main():
    N: int = int(input())
    A: List[int] = [0 for i in range(N - 1)]
    B: List[int] = [0 for i in range(N - 1)]
    graph: List[List[int]] = [[] for i in range(N)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        A[i] = a
        B[i] = b
        graph[a].append(b)
        graph[b].append(a)

    dp: List[int] = [1 << 60 for i in range(N)]
    dfs(graph, dp, 0, -1)

    answer: int = 0
    for a, b in zip(A, B):
        r: int = min(dp[a], dp[b])
        answer += r * (N - r)

    print(answer)


if __name__ == "__main__":
    main()
