from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    until: bool = True
    while until:
        has_changed: bool = False
        for i in range(N - 1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                has_changed = True

        if has_changed is False:
            until = False
            break
        print(" ".join(map(str, A)))


if __name__ == "__main__":
    main()
