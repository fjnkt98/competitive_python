from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N = int(input())
    A: List[Tuple[int, int]] = [() for i in range(N)]
    for i in range(N):
        s, t = map(int, input().split())
        A[i] = (s, t)

    A.sort(key=lambda a: a[1])

    last_endpoint: int = 0
    answer: int = 0
    for s, t in A:
        if s <= last_endpoint:
            continue
        last_endpoint = t
        answer += 1

    print(answer)


if __name__ == "__main__":
    main()
