from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, P, Q = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    A = list(map(lambda x: x % P, A))

    answer: int = 0
    for a in itertools.combinations(A, 5):
        prod: int = 1
        for ai in a:
            prod *= ai
            prod %= P
        if prod % P == Q:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
