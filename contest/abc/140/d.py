from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    S: str = input().rstrip()

    rlc: List[Tuple[str, int]] = [(k, len(list(v))) for k, v in itertools.groupby(S)]

    size: int = len(rlc)
    for i in range(K):
        if size >= 3:
            size -= 2
        elif size == 2:
            size = 1

    print(N - size)


if __name__ == "__main__":
    main()
