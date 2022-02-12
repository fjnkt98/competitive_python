from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(10000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    dp: List[List[int]] = [[int(1e18) for i in range(N)] for i in range(N)]

    for i in range(M):
        s, t, d = map(int, input().split())
        dp[s][t] = d

    for i in range(N):
        dp[i][i] = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    for i in range(N):
        if dp[i][i] < 0:
            print("NEGATIVE CYCLE")
            return

    for i in range(N):
        output = ["INF" if d >= int(1e15) else d for d in dp[i]]

        print(" ".join(map(str, output)))


if __name__ == "__main__":
    main()
