class EratosthenesSieve:
    """
    Class implementation of eratosthenes sieve
    """

    def __init__(self, N: int) -> None:
        """
        Constructor takes length of sieve
        """
        self._N: int = N
        self._is_prime: list[bool] = [True for i in range(N + 1)]
        self._primes: list[int] = []
        self._minimum_factor_of: list[int] = [-1 for i in range(N + 1)]

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

    def factorize(self, N: int) -> list[tuple[int, int]]:
        """
        Returns a list of pair of N prime factors and their exponents.
        """
        if N > self._N:
            return []

        result: list[tuple[int, int]] = []
        while N > 1:
            p: int = self._minimum_factor_of[N]
            exp: int = 0

            while self._minimum_factor_of[N] == p:
                N //= p
                exp += 1

            result.append((p, exp))

        return result

    def divisors(self, N: int) -> list[int]:
        """
        Returns a list of N's divisors.
        """
        if N > self._N:
            return []

        result: list[int] = [1]
        factors: list[tuple[int, int]] = self.factorize(N)

        for p, exp in factors:
            size: int = len(result)
            for i in range(size):
                v: int = 1
                for j in range(exp):
                    v *= p
                    result.append(result[i] * v)

        return sorted(result)

    def primes(self) -> list[int]:
        """
        Returns a list of prime numbers up to N.
        """
        return self._primes

    def is_prime(self) -> list[bool]:
        """
        Returns a list of boolean indicating whether the number is prime or not up to N.
        """
        return self._is_prime


def main() -> None:
    Q: int = int(input())
    X = [int(input()) for _ in range(Q)]

    es = EratosthenesSieve(max(X))
    is_prime = es.is_prime()

    for x in X:
        print("Yes" if is_prime[x] else "No")


if __name__ == "__main__":
    main()
