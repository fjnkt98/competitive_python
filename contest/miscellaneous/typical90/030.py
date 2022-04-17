from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())

    count: List[int] = [0] * (N + 1)
    for i in range(2, N + 1):
        if count[i] >= 1:
            continue
        for j in range(i, N + 1, i):
            count[j] += 1

    answer: int = 0
    for c in count[1:]:
        if c >= K:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
