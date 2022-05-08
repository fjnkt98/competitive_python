from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)


def main():
    S: str = input()
    T: str = input()

    N: int = len(S)
    M: int = len(T)

    dp: List[List[int]] = [[1 << 60] * (M + 1) for i in range(N + 1)]
    dp[0][0] = 0

    for i in range(N + 1):
        for j in range(M + 1):
            if i > 0 and j > 0:
                if S[i - 1] == T[j - 1]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
                else:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)

            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)

    print(dp[N][M])


if __name__ == "__main__":
    main()
