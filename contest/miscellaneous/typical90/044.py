from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, Q = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    query: List[List[int]] = [list(map(int, input().split())) for i in range(Q)]

    head: int = N - 1
    for t, x, y in query:
        if t == 1:
            A[(x + head) % N], A[(y + head) % N] = A[(y + head) % N], A[(x + head) % N]
        elif t == 2:
            head -= 1
            if head < 0:
                head += N
        else:
            print(A[(x + head) % N])


if __name__ == "__main__":
    main()
