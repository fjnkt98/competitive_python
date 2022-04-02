from typing import List, Tuple, Set
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


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


def main():
    K: int = int(input())

    d: List[int] = divisors(K)

    answer: int = 0

    for a, b in itertools.combinations_with_replacement(d, 2):
        if K % (a * b) == 0:
            c: int = K // (a * b)
            if b <= c:
                answer += 1

    print(answer)


if __name__ == "__main__":
    main()
