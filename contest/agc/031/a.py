from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    S: str = input().rstrip()

    count = collections.Counter(S)
    answer: int = 1
    mod: int = 1000000007
    for key, value in count.items():
        answer *= value + 1
        answer %= mod

    answer -= 1
    print(answer)


if __name__ == "__main__":
    main()
