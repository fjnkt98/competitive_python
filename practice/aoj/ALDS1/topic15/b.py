from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, W = map(int, input().split())
    v: List[int] = [0 for i in range(N)]
    w: List[int] = [0 for i in range(N)]
    for i in range(N):
        v[i], w[i] = map(int, input().split())

    L: List[Tuple[float, int, int]] = [() for i in range(N)]
    for i in range(N):
        L[i] = (v[i] / w[i], v[i], w[i])

    L.sort(reverse=True)

    answer: float = 0
    for ri, vi, wi in L:
        if W <= 0:
            break
        amount = min(W, wi)
        answer += ri * amount
        W -= amount

    print(answer)


if __name__ == "__main__":
    main()
