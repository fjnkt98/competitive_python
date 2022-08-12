from typing import (
    List,
    Tuple,
    Deque,
    Set,
    Dict,
    TypeVar,
    Callable,
    Generic,
    Iterable,
    Iterator,
    Union,
)
import sys
import collections
import itertools
import bisect
import math


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    graph: List[List[int]] = [[1 << 60 for j in range(N)] for i in range(N)]
    for i in range(M):
        s, t, d, _ = map(int, input().split())
        graph[s - 1][t - 1] = d

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
