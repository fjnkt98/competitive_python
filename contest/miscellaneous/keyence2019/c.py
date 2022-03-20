from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))
    B: List[int] = list(map(int, input().split()))

    if sum(A) < sum(B):
        print(-1)
        return

    D: List[int] = [a - b for a, b in zip(A, B)]
    outs: List[int] = list(filter(lambda x: x < 0, D))

    if len(outs) == 0:
        print(0)
        return

    answer: int = len(outs)
    diff: int = sum(outs)

    for d in sorted(list(filter(lambda x: x > 0, D)), reverse=True):
        diff += d
        answer += 1
        if diff >= 0:
            break

    print(answer)


if __name__ == "__main__":
    main()
