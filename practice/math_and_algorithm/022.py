from typing import List, Tuple
import sys
from array import array
import collections


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N = int(input())
    A: List[int] = list(map(int, input().split()))

    count = collections.Counter(A)

    answer: int = 0
    for a in sorted(list(set(A))):
        if a > 50000:
            break
        if a == 50000:
            answer += count[a] * (count[a] - 1) // 2
        else:
            answer += count[a] * count[100000 - a]

    print(answer)


if __name__ == "__main__":
    main()
