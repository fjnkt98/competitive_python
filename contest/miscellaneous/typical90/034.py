from typing import List, Tuple, Deque, Dict
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    D: Dict[int, int] = {}
    scope: Deque[int] = collections.deque()
    answer: int = 0
    for a in A:
        scope.append(a)
        if a not in D:
            D[a] = 1
        else:
            D[a] += 1

        while D and len(D) > K:
            garbage: int = scope.popleft()
            if garbage in D:
                D[garbage] -= 1
                if D[garbage] == 0:
                    del D[garbage]

        answer = max(answer, len(scope))

    print(answer)


if __name__ == "__main__":
    main()
