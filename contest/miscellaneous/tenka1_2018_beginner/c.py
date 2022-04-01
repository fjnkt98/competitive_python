from typing import List, Tuple, Deque
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def f(A: List[int]) -> int:
    N: int = len(A)

    A1: List[int] = A[: N // 2]
    A2: List[int] = A[N // 2 :]

    result: int = 0

    if N % 2 == 0:
        for a in A2:
            result += 2 * a
        result -= A2[0]

        for a in A1:
            result -= 2 * a
        result += A1[-1]
    else:
        for a in A2:
            result += 2 * a
        result -= A2[0]
        result -= A2[1]

        for a in A1:
            result -= 2 * a

    return result


def g(A: List[int]) -> int:
    N: int = len(A)

    A1: List[int] = A[: (N + 1) // 2]
    A2: List[int] = A[(N + 1) // 2 :]

    result: int = 0
    if N % 2 == 0:
        for a in A2:
            result += 2 * a
        result -= A2[0]

        for a in A1:
            result -= 2 * a
        result += A1[-1]
    else:
        for a in A2:
            result += 2 * a
        for a in A1:
            result -= 2 * a
        result += A1[-1]
        result += A1[-2]

    return result


def main():
    N: int = int(input())
    A: List[int] = [int(input()) for i in range(N)]

    A.sort()

    answer: int = max(f(A), g(A))

    print(answer)


if __name__ == "__main__":
    main()
