from typing import *
import collections
import itertools
import bisect
import math
import sys

sys.setrecursionlimit(1000000)


def main():
    N: int = int(input())
    mod: int = 1000000007
    graph: List[List[int]] = [[] for i in range(N)]
    for i in range(N - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    dp: List[List[int]] = [[0, 0] for i in range(N)]

    def dfs(current: int, previous: int) -> List[int]:
        p0: int = 1
        p1: int = 1
        for next_node in graph[current]:
            if next_node == previous:
                continue

            p = dfs(next_node, current)
            p0 *= sum(p)
            p1 *= p[0]

            p0 %= mod
            p1 %= mod

        dp[current] = [p0, p1]

        return dp[current]

    dfs(0, -1)
    print(sum(dp[0]) % mod)


if __name__ == "__main__":
    main()
