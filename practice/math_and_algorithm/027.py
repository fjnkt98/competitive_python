from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def merge_sort(x: List[int], l: int, r: int) -> None:
    if r - l == 1:
        return

    m: int = (l + r) // 2
    merge_sort(x, l, m)
    merge_sort(x, m, r)

    c1: int = l
    c2: int = m
    count: int = 0
    C: List[int] = []

    while c1 != m or c2 != r:
        if c1 == m:
            C.append(x[c2])
            c2 += 1
        elif c2 == r:
            C.append(x[c1])
            c1 += 1
        else:
            if x[c1] < x[c2]:
                C.append(x[c1])
                c1 += 1
            else:
                C.append(x[c2])
                c2 += 1
        count += 1

    for i in range(count):
        x[l + i] = C[i]


def main():
    N = int(input())
    A: List[int] = list(map(int, input().split()))

    merge_sort(A, 0, N)
    print(" ".join(map(str, A)))


if __name__ == "__main__":
    main()
