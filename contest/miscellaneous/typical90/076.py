from typing import List, Tuple
import sys
import collections
import itertools
import bisect


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    whole: int = sum(A)
    if whole // 10 == 0:
        print("No")
        return

    B: List[int] = A + A
    cumsum: List[int] = list(itertools.accumulate(B))
    ok: bool = False
    for i in range(N):
        index: int = bisect.bisect_left(cumsum, cumsum[i] + whole // 10)

        if index == 2 * N:
            continue

        if cumsum[index] - cumsum[i] == whole // 10:
            ok = True

    print("Yes" if ok else "No")


if __name__ == "__main__":
    main()
