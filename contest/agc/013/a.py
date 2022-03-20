from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    answer: int = 1

    # 1: Monotonically Non-Decreasing, -1: Monotonically Non-Increasing, 0: Neither
    state: int = 0
    for i in range(N - 1):
        if A[i] == A[i + 1]:
            continue

        if state == 0:
            if A[i] < A[i + 1]:
                state = 1
            else:
                state = -1
        elif state == 1:
            if A[i] < A[i + 1]:
                continue
            state = 0
            answer += 1
        else:
            if A[i] > A[i + 1]:
                continue
            state = 0
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
