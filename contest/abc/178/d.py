from typing import *
import collections
import itertools
import bisect
import math


def main():
    S: int = int(input())
    mod: int = 1000000007

    if S == 1:
        print(0)
        return

    dp: List[int] = [0 for j in range(S + 1)]
    dp[0] = 1
    dp[1] = dp[2] = 0
    for i in range(3, S + 1):
        dp[i] = (dp[i - 1] + dp[i - 3]) % mod

    print(dp[S])


if __name__ == "__main__":
    main()
