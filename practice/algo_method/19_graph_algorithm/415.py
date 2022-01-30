from typing import List
from sys import setrecursionlimit


setrecursionlimit(1000000)


def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, -1)

    answer: int = 0
    while X != 0:
        answer += 1
        X = A[X]

    print(answer)


if __name__ == "__main__":
    main()
