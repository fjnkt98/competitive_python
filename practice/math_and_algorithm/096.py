from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    T: List[int] = list(map(int, input().split()))

    S: int = sum(T)

    dp: List[List[bool]] = [[0 for j in range(S + 1)] for i in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = True

    for i in range(1, N + 1):
        for j in range(S + 1):
            dp[i][j] = dp[i][j] | dp[i - 1][j]

            if j - T[i - 1] >= 0:
                dp[i][j] = dp[i][j] | dp[i - 1][j - T[i - 1]]

    answer: int = 0
    for j in range(S // 2, S + 1):
        if dp[N][j]:
            answer = max(j, S - j)
            break

    print(answer)


if __name__ == "__main__":
    main()
