from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, S = map(int, input().split())
    A, B = map(list, zip(*[list(map(int, input().split())) for i in range(N)]))

    dp: List[List[bool]] = [[False for j in range(S + 1)] for i in range(N + 1)]
    dp[0][0] = True
    prev: List[List[int]] = [[-1 for j in range(S + 1)] for i in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(S + 1):
            if j - A[i - 1] >= 0:
                if dp[i - 1][j - A[i - 1]]:
                    dp[i][j] = True
                    prev[i][j] = j - A[i - 1]

            if j - B[i - 1] >= 0:
                if dp[i - 1][j - B[i - 1]]:
                    dp[i][j] = True
                    prev[i][j] = j - B[i - 1]

    if dp[N][S]:
        print("Yes")
        answer: List[str] = []
        n: int = N
        s: int = S
        while n > 0:
            if prev[n][s] == s - A[n - 1]:
                answer.append("H")
            elif prev[n][s] == s - B[n - 1]:
                answer.append("T")

            s = prev[n][s]
            n -= 1

        print("".join(reversed(answer)))

    else:
        print("No")


if __name__ == "__main__":
    main()
