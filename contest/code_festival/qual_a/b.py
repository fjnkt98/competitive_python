from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))
    A = list(map(lambda x: x - 1, A))

    answer: int = 0
    for i, a in enumerate(A):
        if i == A[a]:
            answer += 1

    print(answer // 2)


if __name__ == "__main__":
    main()
