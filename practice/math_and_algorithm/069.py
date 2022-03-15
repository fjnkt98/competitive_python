from typing import List, Tuple
import sys
from array import array
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    a, b, c, d = map(int, input().split())

    answer: int = a * c
    for i in [a, b]:
        for j in [c, d]:
            answer = max(answer, i * j)

    print(answer)


if __name__ == "__main__":
    main()
