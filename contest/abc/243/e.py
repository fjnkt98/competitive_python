from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    dp: List[List[int]] = [[1 << 60 for j in range(N)] for i in range(N)]
    edges: List[Tuple[int]] = [[] for i in range(M)]
    for i in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        dp[a][b] = c
        dp[b][a] = c
        edges[i] = (a, b, c)

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    answer: int = 0
    for a, b, c in edges:
        removable: bool = False
        for i in range(N):
            if dp[a][i] + dp[i][b] <= c:
                removable = True

        if removable:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
