from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())

    S: List[int] = []
    while N != 0:
        S.append(N % 2)

        N = -(-N // -2)

    if not S:
        print(0)
        return

    print("".join(map(str, reversed(S))))


if __name__ == "__main__":
    main()
