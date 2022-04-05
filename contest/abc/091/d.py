from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())

    if K == 0:
        print(N * N)
        return

    answer: int = 0
    for b in range(K + 1, N + 1):
        q, r = divmod(N, b)
        answer += q * max(0, b - K) + max(0, r - K + 1)

    print(answer)


if __name__ == "__main__":
    main()
