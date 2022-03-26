from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A, B, C = map(int, input().split())

    answer: int = 1 << 60
    for i in range(10000):
        for j in range(10000 - i):
            remain: int = N - A * i - B * j
            k: int = remain // C
            if remain >= 0 and remain % C == 0:
                answer = min(answer, i + j + k)

    print(answer)


if __name__ == "__main__":
    main()
