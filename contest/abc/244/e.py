from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, M, K, S, T, X = map(int, input().split())
    S -= 1
    T -= 1
    X -= 1
    mod: int = 998244353
    graph: List[List[int]] = [[] for i in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    dp: List[List[List[int]]] = [[[0] * 2 for j in range(N)] for i in range(K + 1)]
    dp[0][S][0] = 1

    for i in range(K):
        for j in range(N):
            for k in graph[j]:
                if k == X:
                    dp[i + 1][k][0] += dp[i][j][1]
                    dp[i + 1][k][1] += dp[i][j][0]

                    dp[i + 1][k][0] %= mod
                    dp[i + 1][k][1] %= mod
                else:
                    dp[i + 1][k][0] += dp[i][j][0]
                    dp[i + 1][k][1] += dp[i][j][1]

                    dp[i + 1][k][0] %= mod
                    dp[i + 1][k][1] %= mod

    print(dp[K][T][0])


if __name__ == "__main__":
    main()
