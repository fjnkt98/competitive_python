from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))
    B: List[int] = list(map(int, input().split()))

    answer1: int = 0
    answer2: int = 0
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            if a == b:
                if i == j:
                    answer1 += 1
                else:
                    answer2 += 1

    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()
