from typing import *
import collections
import itertools
import bisect
import math


def main():
    S: str = input()
    T: str = input()

    N: int = len(S)
    M: int = len(T)

    dp: List[List[int]] = [[0 for j in range(M + 1)] for i in range(N + 1)]
    prev: List[List[Tuple[int, int]]] = [
        [(-1, -1) for j in range(M + 1)] for i in range(N + 1)
    ]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                prev[i][j] = (i - 1, j - 1)
            else:
                if dp[i - 1][j] < dp[i][j - 1]:
                    dp[i][j] = dp[i][j - 1]
                    prev[i][j] = (i, j - 1)
                else:
                    dp[i][j] = dp[i - 1][j]
                    prev[i][j] = (i - 1, j)

    answer: List[str] = []
    i: int = N
    j: int = M
    while len(answer) < dp[N][M]:
        if S[i - 1] == T[j - 1]:
            answer.append(S[i - 1])
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            j -= 1

    print("".join(reversed(answer)))


if __name__ == "__main__":
    main()
