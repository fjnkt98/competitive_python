from typing import List
import sys


sys.setrecursionlimit(10000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    B: List[int] = list(map(int, input().split()))

    answer: int = 0
    for a in A:
        for b in B:
            answer += a + b

    print(answer)


if __name__ == "__main__":
    main()
