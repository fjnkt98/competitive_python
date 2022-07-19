from typing import (
    List,
    Tuple,
    Deque,
    Set,
    Dict,
    TypeVar,
    Callable,
    Generic,
    Iterable,
    Iterator,
    Union,
)
import sys
import collections
import itertools
import bisect
import math


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


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
    N, A, B = map(int, input().split())
    V: List[int] = sorted(list(map(int, input().split())), reverse=True)

    C = collections.Counter(V)

    comb: List[List[int]] = []
    max_mean: float = 0.0
    for i in range(A, B + 1):
        mean: float = sum(V[:i]) / i
        if mean >= max_mean:
            max_mean = mean
            comb.append(V[:i])

    bc = BinominalCoefficient(N + 1, 1000000000000000003)

    answer: int = 0
    for c in comb:
        count = collections.Counter(c)

        a = 1
        for k, v in count.items():
            a *= bc.nCr(C[k], v)

        answer += a

    print(max_mean)
    print(answer)


if __name__ == "__main__":
    main()
