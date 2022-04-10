from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    answer: List[int] = [0] * 5
    for a in A:
        if 0 <= a <= 20:
            answer[0] += 1
        elif a <= 40:
            answer[1] += 1
        elif a <= 60:
            answer[2] += 1
        elif a <= 80:
            answer[3] += 1
        else:
            answer[4] += 1

    for a in answer:
        print(a)


if __name__ == "__main__":
    main()
