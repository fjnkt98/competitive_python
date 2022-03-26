from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, Q = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    diff: List[int] = [0] * (N)
    for i in range(N - 1):
        diff[i + 1] = A[i + 1] - A[i]

    inconvenience: int = sum(list(map(lambda x: abs(x), diff)))

    answer: List[int] = []
    for i in range(Q):
        l, r, v = map(int, input().split())
        l -= 1
        r -= 1

        if l != 0:
            inconvenience -= abs(diff[l])
            diff[l] += v
            inconvenience += abs(diff[l])

        if r != N - 1:
            inconvenience -= abs(diff[r + 1])
            diff[r + 1] -= v
            inconvenience += abs(diff[r + 1])

        answer.append(inconvenience)

    for a in answer:
        print(a)


if __name__ == "__main__":
    main()
