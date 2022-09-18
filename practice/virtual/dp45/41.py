from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M = map(int, input().split())
    S: List[int] = [0] * M
    C: List[int] = [0] * M
    for i in range(M):
        s, c = input().split()
        S[i] = int("".join(["1" if x == "Y" else "0" for x in s]), 2)
        C[i] = int(c)

    dp: List[int] = [1 << 60 for i in range(1 << N)]
    dp[0] = 0
    for bits in range(1 << N):
        for i in range(M):
            dp[bits | S[i]] = min(dp[bits | S[i]], dp[bits] + C[i])

    answer: int = dp[(1 << N) - 1]
    if answer == 1 << 60:
        print(-1)
    else:
        print(answer)


if __name__ == "__main__":
    main()
