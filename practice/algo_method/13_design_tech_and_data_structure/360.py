from typing import List
import sys


sys.setrecursionlimit(10000)
input = sys.stdin.readline


def main():
    X: int = int(input())
    A: List[int] = list(map(int, input().split()))
    C: List[int] = [50, 10, 5, 1]

    answer: int = 0
    for i in range(4):
        quantity: int = X // C[i]

        quantity = min(quantity, A[i])

        answer += quantity

        X -= C[i] * quantity

    print(answer)


if __name__ == "__main__":
    main()
