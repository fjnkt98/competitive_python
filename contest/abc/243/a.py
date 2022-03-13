from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    V, *A = list(map(int, input().split()))
    answer: int = 0

    remain: int = V
    for i in range(V + 100):
        if remain < A[i % 3]:
            answer = i % 3
            break
        else:
            remain -= A[i % 3]

    if answer == 0:
        print("F")
    elif answer == 1:
        print("M")
    else:
        print("T")


if __name__ == "__main__":
    main()
