from typing import List, Tuple
import sys
from array import array
import itertools

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))
    M: int = int(input())
    B: List[int] = [0 for i in range(M)]
    for i in range(M):
        B[i] = int(input())

    A.insert(0, 0)
    A.insert(0, 0)
    C = list(itertools.accumulate(A))

    answer: int = 0
    current: int = B[0]
    for b in B[1:]:
        answer += abs(C[b] - C[current])
        current = b

    print(answer)


if __name__ == "__main__":
    main()
