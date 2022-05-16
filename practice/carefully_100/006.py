from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    S: str = input().rstrip()

    answer: int = 0
    for n in range(1000):
        m: str = str(n).zfill(3)

        i: int = 0
        for s in S:
            if s == m[i]:
                i += 1

            if i >= 3:
                break

        if i >= 3:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
