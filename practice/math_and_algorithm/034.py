from typing import List, Tuple
import sys
from array import array
import itertools
import math


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N = int(input())
    P: List[Tuple[int, int]] = [() for i in range(N)]
    for i in range(N):
        x, y = map(int, input().split())
        P[i] = (x, y)

    answer: float = 1e9
    for p1, p2 in itertools.combinations(P, 2):
        x1, y1 = p1
        x2, y2 = p2

        answer = min(answer, math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))

    print(answer)


if __name__ == "__main__":
    main()
