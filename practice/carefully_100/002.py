from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
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
    N: int = int(input())

    answer: int = 0
    for i in range(1, N + 1):
        if i % 2 == 1 and len(divisors(i)) == 8:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
