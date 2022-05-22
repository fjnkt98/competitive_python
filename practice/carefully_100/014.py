from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    answer: int = 1 << 60
    for bits in itertools.product((0, 1), repeat=N - 1):
        cost: int = 0
        B: List[int] = A.copy()
        height: int = B[0]
        for i, bit in enumerate(bits):
            if bit == 1 and B[i + 1] <= height:
                diff: int = height - B[i + 1] + 1
                B[i + 1] += diff
                cost += diff
            height = max(height, B[i + 1])

        count: int = 1
        height = B[0]
        for b in B[1:]:
            if b > height:
                count += 1
                height = b

        if count >= K:
            answer = min(answer, cost)

    print(answer)


if __name__ == "__main__":
    main()
