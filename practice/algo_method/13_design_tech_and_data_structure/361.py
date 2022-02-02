from typing import List
import sys


sys.setrecursionlimit(10000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    A: List[int] = list(map(int, input().split()))
    B: List[int] = list(map(int, input().split()))

    answer: int = 0
    used: List[bool] = [False for i in range(N)]

    for j in range(M):
        for i in range(N):
            if used[i]:
                continue

            if A[i] <= B[j]:
                answer += 1
                used[i] = True

                break

    print(answer)


if __name__ == "__main__":
    main()
