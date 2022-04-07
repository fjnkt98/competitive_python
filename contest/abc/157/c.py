from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    P: List[Tuple[int, int]] = [tuple(map(int, input().split())) for i in range(M)]

    answer: List[int] = []
    for i in range(10 ** N):
        S: str = str(i)
        if len(S) != N:
            continue

        ok: bool = True
        for s, c in P:
            if int(S[s - 1]) != c:
                ok = False
        if ok:
            answer.append(i)

    answer.sort()
    if len(answer) == 0:
        print(-1)
    else:
        print(answer[0])


if __name__ == "__main__":
    main()
