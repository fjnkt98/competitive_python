from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    S: str = input().rstrip()

    N: int = len(S)

    answer: int = 0
    for i, j in itertools.combinations_with_replacement(range(N), 2):
        T: str = S[i : j + 1]

        U: Set[str] = set(T) - {"A", "C", "G", "T"}
        if not U:
            answer = max(answer, len(T))

    print(answer)


if __name__ == "__main__":
    main()
