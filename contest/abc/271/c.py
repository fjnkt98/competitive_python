from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    A: List[int] = sorted(list(map(int, input().split())))

    B: List[int] = []
    C: List[int] = []
    S: Set[int] = set()
    for a in A:
        if a in S:
            C.append(a)
        else:
            B.append(a)
            S.add(a)

    B.extend(C)
    D = collections.deque(B)

    current: int = 1
    answer: int = 0
    while D:
        if D[0] == current:
            D.popleft()
            answer += 1
            current += 1
        else:
            if len(D) >= 2:
                D.pop()
                D.pop()
                answer += 1
                current += 1
            else:
                break

    print(answer)


if __name__ == "__main__":
    main()
