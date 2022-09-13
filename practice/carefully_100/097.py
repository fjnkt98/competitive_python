from typing import *
import collections
import itertools
import bisect
import math
import functools
import operator


def lcm(a: int, b: int) -> int:
    return (a * b) // math.gcd(a, b)


def main():
    N, M = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    B: List[int] = [a // 2 for a in A]
    C: List[int] = [0 for i in range(N)]
    for i, a in enumerate(A):
        count: int = 0
        while a % 2 == 0:
            a //= 2
            count += 1
        C[i] = count

    if len(set(C)) != 1:
        print(0)
        return

    answer: int = ((M // functools.reduce(lcm, B)) + 1) // 2
    print(answer)


if __name__ == "__main__":
    main()
