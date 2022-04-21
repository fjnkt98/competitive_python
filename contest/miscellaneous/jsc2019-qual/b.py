from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    mod: int = 1000000007

    inner_inversion: int = 0
    for ai, aj in itertools.combinations(A, 2):
        if ai > aj:
            inner_inversion += 1

    count_less: int = 0
    for ai, aj in itertools.product(A, repeat=2):
        if ai > aj:
            count_less += 1

    answer: int = (K * inner_inversion) % mod
    answer += ((K * (K - 1) // 2) * count_less) % mod
    answer %= mod
    print(answer)


if __name__ == "__main__":
    main()
