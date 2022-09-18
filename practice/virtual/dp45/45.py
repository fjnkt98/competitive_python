from typing import *
import collections
import itertools
import bisect
import math


def main():
    H, W, K = map(int, input().split())
    mod: int = 1000000007

    def check(X: List[int]) -> bool:
        Y: List[int] = [len(list(v)) for k, v in itertools.groupby(X) if k == 1]
        return len(list(filter(lambda y: y >= 2, Y))) == 0

    dp: List[List[int]] = [[0 for j in range(W + 1)] for i in range(H + 1)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            dp[i][j] %= mod
            for bits in itertools.product((0, 1), repeat=W - 1):
                if not check(list(bits)):
                    continue

                bits = bits + (0,)
                if bits[j] == 1:
                    dp[i + 1][j + 1] += dp[i][j]
                elif bits[j - 1] == 1:
                    dp[i + 1][j - 1] += dp[i][j]
                else:
                    dp[i + 1][j] += dp[i][j]

    print(dp[H][K - 1] % mod)


if __name__ == "__main__":
    main()
