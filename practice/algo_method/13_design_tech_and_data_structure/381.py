from typing import List
import sys
import bisect


sys.setrecursionlimit(10000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    A.sort()
    answer: int = 0
    for a in A:
        answer += N - bisect.bisect_left(A, K - a)

    print(answer)


if __name__ == "__main__":
    main()
