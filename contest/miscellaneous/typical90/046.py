from typing import List, Tuple, Counter
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))
    B: List[int] = list(map(int, input().split()))
    C: List[int] = list(map(int, input().split()))

    AM: Counter[int, int] = collections.Counter(list(map(lambda x: x % 46, A)))
    BM: Counter[int, int] = collections.Counter(list(map(lambda x: x % 46, B)))
    CM: Counter[int, int] = collections.Counter(list(map(lambda x: x % 46, C)))

    answer: int = 0
    for a, x in AM.items():
        for b, y in BM.items():
            for c, z in CM.items():
                if (a + b + c) % 46 == 0:
                    answer += x * y * z

    print(answer)


if __name__ == "__main__":
    main()
