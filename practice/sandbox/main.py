from typing import List, Tuple
import sys
import bisect
import math
from array import array

sys.setrecursionlimit(10000)
input = sys.stdin.readline


class EratosthenesSieve:
    """
    Class implementation of eratosthenes sieve
    """

    def __init__(self, N: int):
        """
        Constructor takes length of sieve
        """
        self._N: int = N
        self._is_prime: List[bool] = [True for i in range(N + 1)]
        self._primes: List[int] = []
        self._minimum_factor_of: List[int] = [-1 for i in range(N + 1)]

        self._is_prime[0] = self._is_prime[1] = False
        self._minimum_factor_of[1] = 1

        for i in range(2, N + 1):
            if not self._is_prime[i]:
                continue

            self._primes.append(i)
            self._minimum_factor_of[i] = i

            for j in range(2 * i, N + 1, i):
                self._is_prime[j] = False

                if self._minimum_factor_of[j] == -1:
                    self._minimum_factor_of[j] = i

    def factorize(self, N: int) -> List[Tuple[int, int]]:
        """
        Returns a list of pair of N prime factors and their exponents.
        """
        if N > self._N:
            return []

        result: List[Tuple[int, int]] = []
        while N > 1:
            p: int = self._minimum_factor_of[N]
            exp: int = 0

            while self._minimum_factor_of[N] == p:
                N //= p
                exp += 1

            result.append((p, exp))

        return result

    def divisors(self, N: int) -> List[int]:
        """
        Returns a list of N's divisors.
        """
        if N > self._N:
            return []

        result: List[int] = [1]
        factors: List[Tuple[int, int]] = self.factorize(N)

        for p, exp in factors:
            size: int = len(factors)
            for i in range(size):
                v: int = 1
                for j in range(exp):
                    v *= p
                    result.append(result[i] * v)

        return sorted(result)

    def primes(self) -> List[int]:
        """
        Returns a list of prime numbers up to N.
        """
        return self._primes

    def is_prime(self) -> List[bool]:
        """
        Returns a list of boolean indicating whether the number is prime or not up to N.
        """
        return self._is_prime


def divisors(N: int) -> List[int]:
    result: List[int] = []

    i: int = 1
    while i * i <= N:
        if N % i == 0:
            result.append(i)

            if N // i != i:
                result.append(N // i)
        i += 1

    return sorted(result)


def factorize(N: int) -> List[Tuple[int, int]]:
    result: List[Tuple[int, int]] = []

    i: int = 2
    while i * i <= N:
        if N % i == 0:
            exp: int = 0

            while N % i == 0:
                N //= i
                exp += 1

            result.append((i, exp))
        i += 1

    if N != 1:
        result.append((N, 1))

    return result


def main():
    es = EratosthenesSieve(30)

    print(es.is_prime())


if __name__ == "__main__":
    main()
