from typing import List, Tuple, Deque
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    answer: int = 0
    cumsum: List[int] = list(itertools.accumulate(A))

    count = collections.defaultdict(int)
    count[0] = 1
    for i, a in enumerate(A):
        answer += count[cumsum[i] % M]
        count[cumsum[i] % M] += 1

    print(answer)


if __name__ == "__main__":
    main()
