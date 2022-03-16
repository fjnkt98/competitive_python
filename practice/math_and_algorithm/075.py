from typing import List, Tuple
import sys
from array import array


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
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    mod: int = 1000000007
    bc = BinominalCoefficient(N, mod)

    answer: int = 0
    for i in range(N):
        answer += A[i] * bc.nCr(N - 1, i)
        answer %= mod

    print(answer)


if __name__ == "__main__":
    main()
