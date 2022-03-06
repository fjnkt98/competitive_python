from typing import List, Tuple
import sys
from array import array


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
    N = int(input())

    for d in divisors(N):
        print(d)


if __name__ == "__main__":
    main()
