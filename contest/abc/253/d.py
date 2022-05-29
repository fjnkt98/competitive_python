from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools
import math


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def f(a: int, d: int, n: int) -> int:
    return (2 * a + (n - 1) * d) * n // 2


def main():
    N, A, B = map(int, input().split())

    answer: int = N * (N + 1) // 2

    gcd: int = math.gcd(A, B)
    lcm: int = A * B // gcd

    answer -= f(A, A, N // A)
    answer -= f(B, B, N // B)
    answer += f(lcm, lcm, N // lcm)

    print(answer)


if __name__ == "__main__":
    main()
