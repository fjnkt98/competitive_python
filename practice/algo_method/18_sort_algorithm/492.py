from typing import List, Tuple, Dict
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    B: List[int] = sorted(set(A), reverse=True)
    D: Dict[int, int] = {v: i for i, v in enumerate(B)}

    for a in A:
        print(D[a])


if __name__ == "__main__":
    main()
