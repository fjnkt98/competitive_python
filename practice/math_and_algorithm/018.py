from typing import List, Tuple
import sys
from array import array
import collections


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))

    count = collections.Counter(A)
    print(count[100] * count[400] + count[200] * count[300])


if __name__ == "__main__":
    main()
