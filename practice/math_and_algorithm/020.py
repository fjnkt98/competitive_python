from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N = int(input())
    A = array("q", list(map(int, input().split())))

    answer: int = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                for l in range(k + 1, N):
                    for m in range(l + 1, N):
                        if A[i] + A[j] + A[k] + A[l] + A[m] == 1000:
                            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
