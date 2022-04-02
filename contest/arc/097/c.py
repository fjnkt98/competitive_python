from typing import List, Tuple, Set
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    S: str = input().rstrip()
    K: int = int(input())

    result: Set[str] = set()
    for i in range(len(S)):
        for j in range(1, 6):
            result.add(S[i : i + j])

    print(list(sorted(list(result)))[K - 1])


if __name__ == "__main__":
    main()
