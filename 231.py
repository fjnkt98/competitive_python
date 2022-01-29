from typing import List
import itertools


def main():
    N, M = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    B: List[int] = list(map(int, input().split()))

    count: int = 0

    for a, b in itertools.product(A, B):
        if a > b:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
