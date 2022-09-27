from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    graph: List[List[int]] = [[1 << 60 for j in range(N)] for i in range(N)]
    X, Y, Z = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))
    for i, j in itertools.combinations(range(N), r=2):
        graph[i][j] = abs(X[i] - X[j]) + abs(Y[i] - Y[j]) + max(0, Z[j] - Z[i])
        graph[j][i] = abs(X[i] - X[j]) + abs(Y[i] - Y[j]) + max(0, Z[i] - Z[j])

    dp: List[List[int]] = [[1 << 60 for j in range(N)] for i in range(2 ** N)]
    dp[0][0] = 0

    for bits in itertools.product((0, 1), repeat=N):
        S: int = int("".join(map(str, bits)), 2)

        for v, u in itertools.product(range(N), repeat=2):
            if bits[N - u - 1] == 0 and S != 0:
                continue
            if bits[N - v - 1] == 0:
                dp[S | (1 << v)][v] = min(dp[S | (1 << v)][v], dp[S][u] + graph[u][v])

    if dp[-1][0] == 1 << 60:
        print(-1)
    else:
        print(dp[-1][0])


if __name__ == "__main__":
    main()
