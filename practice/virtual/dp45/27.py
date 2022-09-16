from typing import *
import collections
import itertools
import bisect
import math


class BinominalCoefficient:
    def __init__(self, N: int, mod: int):
        self._N: int = N
        self._mod: int = mod
        self._factorial: List[int] = [1 for i in range(N + 1)]
        self._inverse_element: List[int] = [1 for i in range(N + 1)]
        self._inverse_factorial: List[int] = [1 for i in range(N + 1)]

        for i in range(2, self._N + 1):
            self._factorial[i] = self._factorial[i - 1] * i % self._mod
            self._inverse_element[i] = (
                self._mod
                - self._inverse_element[self._mod % i] * (self._mod // i) % self._mod
            )
            self._inverse_factorial[i] = (
                self._inverse_factorial[i - 1] * self._inverse_element[i] % self._mod
            )

    def nCr(self, n: int, r: int) -> int:
        if n > self._N or n < r or n < 0 or r < 0:
            return 0

        return (
            self._factorial[n]
            * (self._inverse_factorial[r] * self._inverse_factorial[n - r] % self._mod)
            % self._mod
        )


def main():
    S: int = int(input())
    mod: int = 1000000007

    bc = BinominalCoefficient(S, mod)
    answer: int = 0
    for k in range(1, S // 3 + 1):
        answer += bc.nCr(S - 2 * k - 1, k - 1)
        answer %= mod

    print(answer % mod)


if __name__ == "__main__":
    main()
