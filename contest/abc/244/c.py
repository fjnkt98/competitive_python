from typing import List, Tuple, Set
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())

    available: Set[int] = {i for i in range(1, 2 * N + 2)}
    while True:
        print(available.pop(), flush=True)
        aoki: int = int(input())
        available.discard(aoki)

        if aoki == 0:
            break


if __name__ == "__main__":
    main()
