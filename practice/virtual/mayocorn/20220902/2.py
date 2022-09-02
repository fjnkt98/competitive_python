from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, K = map(int, input().split())
    C: List[int] = list(map(int, input().split()))

    S: Set[int] = set(C[:K])
    count = collections.Counter(C[:K])
    answer: int = len(S)
    for i in range(K, N):
        S.add(C[i])
        count[C[i]] += 1

        count[C[i - K]] -= 1
        if count[C[i - K]] == 0:
            S.remove(C[i - K])

        answer = max(answer, len(S))

    print(answer)


if __name__ == "__main__":
    main()
