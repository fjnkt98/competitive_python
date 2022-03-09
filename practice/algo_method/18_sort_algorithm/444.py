from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def merge_sort(A: List[int]) -> List[int]:
    if len(A) <= 1:
        return A
    mid: int = len(A) // 2

    L: List[int] = A[:mid]
    R: List[int] = A[mid:]

    L = merge_sort(L)
    R = merge_sort(R)

    L.reverse()
    R.reverse()

    B: List[int] = []
    while L or R:
        if L and R:
            if L[-1] < R[-1]:
                B.append(L.pop())
            else:
                B.append(R.pop())
        elif len(L) == 0:
            while R:
                B.append(R.pop())
        else:
            while L:
                B.append(L.pop())

    return B


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    A = merge_sort(A)

    print(" ".join(map(str, A)))


if __name__ == "__main__":
    main()
