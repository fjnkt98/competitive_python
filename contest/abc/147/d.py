from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    bitcount: List[int] = [[0] * N for i in range(64)]
    for i, a in enumerate(A):
        for j in range(64):
            if a & (1 << j):
                bitcount[j][i] += 1

    answer: int = 0
    mod: int = 1000000007
    for i, b in enumerate(bitcount):
        count = collections.Counter(b)

        answer += count[0] * count[1] * (1 << i)
        answer %= mod

    print(answer % mod)


if __name__ == "__main__":
    main()
