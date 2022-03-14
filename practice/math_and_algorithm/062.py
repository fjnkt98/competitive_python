from typing import List, Tuple, DefaultDict
import sys
from array import array
import collections


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    D: DefaultDict[int, int] = collections.defaultdict(int)
    A.insert(0, 1)

    answer: int = 1
    loop_start: int = -1
    loop_end: int = -1
    i: int = 0

    while K:
        answer = A[answer]
        if D[answer] != 0:
            loop_start = D[answer]
            loop_end = i
            K -= 1
            break

        D[answer] = i

        K -= 1
        i += 1

    if K > 0:
        K = K % (loop_end - loop_start)

        while K:
            answer = A[answer]
            K -= 1

    print(answer)


if __name__ == "__main__":
    main()
