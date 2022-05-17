from typing import List, Tuple, Deque, Set, Dict, TypeVar, Callable, Generic
import sys
import collections
import itertools
import bisect


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    X, Y = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    B: List[int] = list(map(int, input().split()))

    port: int = 0
    time: int = 0
    answer: int = 0

    while True:
        if port == 0:
            i: int = bisect.bisect_left(A, time)
            if i >= N:
                break
            time = A[i] + X
        else:
            i: int = bisect.bisect_left(B, time)
            if i >= M:
                break
            time = B[i] + Y

        port = 1 - port
        if port == 0:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
