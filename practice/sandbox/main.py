from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, X = map(int, input().split())
    W, V = zip(*[tuple(map(int, input().split())) for i in range(N)])
    W: List[int] = [0] + list(W)
    V: List[int] = [0] + list(V)

    dp: List[List[int]] = [[0 for j in range(X + 1)] for i in range(N + 1)]
    re: List[List[int]] = [[-1 for i in range(X + 1)] for i in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(X + 1):
            if dp[i][j] < dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
                re[i][j] = j

            if j - W[i] >= 0:
                if dp[i][j] < dp[i - 1][j - W[i]] + V[i]:
                    dp[i][j] = dp[i - 1][j - W[i]] + V[i]
                    re[i][j] = j - W[i]

    answer: int = dp[N][X]
    select: List[int] = []
    x: int = X
    for i in range(N, 0, -1):
        if re[i][x] == x - W[i]:
            select.append(i)

        x = re[i][x]

    print(answer)
    print(select)


if __name__ == "__main__":
    main()
