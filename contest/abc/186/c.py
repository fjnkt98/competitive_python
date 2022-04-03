from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())

    answer: int = 0
    for i in range(1, N + 1):
        if "7" in str(i) or "7" in oct(i):
            continue
        answer += 1

    print(answer)


if __name__ == "__main__":
    main()
