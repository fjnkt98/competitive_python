from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())
    P: List[int] = list(map(int, input().split()))

    answer: List[int] = []
    i: int = 0
    while i < 2 * N - 2:
        if i % 2 == 0:
            if P[i] > P[i + 1]:
                if P[i] > P[i + 2]:
                    P[i], P[i + 1] = P[i + 1], P[i]
                    answer.append(i)
                    i += 2
                else:
                    P[i + 1], P[i + 2] = P[i + 2], P[i + 1]
                    answer.append(i + 1)
                    i += 2
            else:
                i += 1
        else:
            if P[i] < P[i + 1]:
                if P[i] > P[i + 2]:
                    P[i + 1], P[i + 2] = P[i + 2], P[i + 1]
                    answer.append(i + 1)
                    i += 2
                else:
                    P[i], P[i + 1] = P[i + 1], P[i]
                    answer.append(i)
                    i += 2
            else:
                i += 1

    if i < 2 * N - 1:
        if i % 2 == 0:
            if P[i] > P[i + 1]:
                P[i], P[i + 1] = P[i + 1], P[i]
                answer.append(i)
        else:
            if P[i] < P[i + 1]:
                P[i], P[i + 1] = P[i + 1], P[i]
                answer.append(i)

    print(len(answer))
    if answer:
        print(*[a + 1 for a in answer])


if __name__ == "__main__":
    main()
