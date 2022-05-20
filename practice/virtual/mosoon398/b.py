from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    A, B, C, K = map(int, input().split())

    answer: int = 0
    if A >= K:
        answer += K
    else:
        answer += A
        K -= A

        if K > B:
            K -= B
            answer -= K

    print(answer)


if __name__ == "__main__":
    main()
