from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    count = collections.Counter(A)
    common = count.most_common(len(count))

    frequency: int = common[0][1]
    answer: List[int] = []
    for key, value in common:
        if value == frequency:
            answer.append(key)
        else:
            break

    for a in sorted(answer):
        print(a)


if __name__ == "__main__":
    main()
