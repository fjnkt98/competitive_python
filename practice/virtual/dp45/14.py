from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, Ma, Mb = map(int, input().split())
    A, B, C = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))
    A.insert(0, 0)
    B.insert(0, 0)
    C.insert(0, 0)

    dp: List[List[List[int]]] = [
        [[1 << 60] * (500) for j in range(500)] for i in range(N + 1)
    ]
    dp[0][0][0] = 0
    for i in range(1, N + 1):
        for j in range(500):
            for k in range(500):
                dp[i][j][k] = dp[i - 1][j][k]

                if j - A[i] >= 0 and k - B[i] >= 0:
                    dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j - A[i]][k - B[i]] + C[i])

    answer: int = 1 << 60
    for i in range(1, 100):
        a: int = Ma * i
        b: int = Mb * i

        if a >= 500 or b >= 500:
            break

        answer = min(answer, dp[N][a][b])

    if answer == 1 << 60:
        print(-1)
    else:
        print(answer)


if __name__ == "__main__":
    main()
