from typing import *
import collections
import itertools
import bisect
import math


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


def f(A: int, B: int) -> int:
    return max(len(str(A)), len(str(B)))


def main():
    N: int = int(input())

    D: List[int] = divisors(N)

    answer: int = 1 << 60
    for a in D:
        b: int = N // a
        if b == 0:
            continue

        answer = min(answer, f(a, b))

    print(answer)


if __name__ == "__main__":
    main()
