from typing import List, Tuple
import sys
from array import array
import random


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def quick_sort(A: List[int]):
    if len(A) <= 1:
        return A
    X: int = random.randrange(len(A))
    pivot = A[X]

    L: List[int] = []
    R: List[int] = []

    for i, a in enumerate(A):
        if i == X:
            continue
        if a == pivot:
            if random.randrange(2) == 0:
                L.append(a)
            else:
                R.append(a)
        elif a < pivot:
            L.append(a)
        else:
            R.append(a)

    if R:
        R = quick_sort(R)
    if L:
        L = quick_sort(L)

    L.append(pivot)
    L.extend(R)
    return L


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    A = quick_sort(A)

    print(" ".join(map(str, A)))


if __name__ == "__main__":
    main()
