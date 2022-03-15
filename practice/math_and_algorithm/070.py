from typing import List, Tuple
import sys
from array import array
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    P: List[List[int]] = [list(map(int, input().split())) for i in range(N)]

    answer: int = 1 << 63
    for p in itertools.product(P, repeat=4):
        l: int = p[0][0]
        r: int = p[1][0]
        t: int = p[2][1]
        b: int = p[3][1]

        count: int = 0
        for x, y in P:
            if l <= x <= r and b <= y <= t:
                count += 1

        if count >= K:
            answer = min(answer, (r - l) * (t - b))

    print(answer)


if __name__ == "__main__":
    main()
