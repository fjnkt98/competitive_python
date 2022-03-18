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
    N: int = int(input())

    answer: int = 1 << 60

    i: int = 0
    while i * i <= N:
        i += 1
        if N % i != 0:
            continue

        j = N // i

        answer = min(answer, 2 * i + 2 * j)

    print(answer)


if __name__ == "__main__":
    main()
