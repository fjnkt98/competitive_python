from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def factorize(N: int) -> List[int]:
    result: List[int] = []

    i: int = 2
    while i * i <= N:
        while N % i == 0:
            result.append(i)
            N //= i
        i += 1

    if N != 1:
        result.append(N)

    return result


def main():
    N: int = int(input())

    primes: List[int] = factorize(N)
    M: int = len(primes)

    answer: int = 0
    for i in range(20):
        if (1 << i) >= M:
            answer = i
            break

    print(answer)


if __name__ == "__main__":
    main()
