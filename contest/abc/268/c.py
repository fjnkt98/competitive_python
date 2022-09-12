from typing import *


def main():
    N: int = int(input())
    P: List[int] = list(map(int, input().split()))

    C: List[int] = [0] * N
    for i in range(N):
        C[(N - P[i] + i) % N] += 1
        C[(N - P[i] + i - 1) % N] += 1
        C[(N - P[i] + i + 1) % N] += 1

    print(max(C))


if __name__ == "__main__":
    main()
