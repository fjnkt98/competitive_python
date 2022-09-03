from typing import *
import bisect
import sys

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
            size: int = len(result)
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


def main():
    Q: int = int(input())
    L, R = map(list, zip(*[list(map(int, input().split())) for i in range(Q)]))
    # Q: int = random.randint(10, 20)
    # L: List[int] = [random.randint(1, 100) for i in range(Q)]
    # R: List[int] = [random.randint(L[i], 100) for i in range(Q)]

    es = EratosthenesSieve(100001)

    is_prime: List[bool] = es.is_prime()
    A: List[int] = sorted(
        [p for p in es.primes() if is_prime[p] and is_prime[(p + 1) // 2]]
    )

    for l, r in zip(L, R):
        i: int = bisect.bisect_left(A, l)
        j: int = bisect.bisect_right(A, r)
        print(j - i)


if __name__ == "__main__":
    main()
