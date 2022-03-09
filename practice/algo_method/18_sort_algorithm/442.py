from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def quick_sort(A: List[int]):
    X: int = len(A) // 2
    pivot = A[X]

    L: List[int] = []
    R: List[int] = []

    for i, a in enumerate(A):
        if i == X:
            continue
        if a < pivot:
            L.append(a)
        else:
            R.append(a)

    if R:
        R = quick_sort(R)
    if L:
        L = quick_sort(L)

    return L + [pivot] + R


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    A = quick_sort(A)

    print(" ".join(map(str, A)))


if __name__ == "__main__":
    main()
