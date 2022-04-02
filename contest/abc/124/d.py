from typing import List, Tuple, Deque
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    S: str = input().rstrip()

    groups: List[Tuple[str, int]] = [(k, len(list(v))) for k, v in itertools.groupby(S)]

    answer: int = 0
    scope: Deque[Tuple[int, int]] = collections.deque()
    s: int = 0
    z: int = 0
    for g in groups:
        scope.append(g)
        s += g[1]
        if g[0] == "0":
            z += 1

        while z > K:
            if scope[0][0] == "0":
                z -= 1
            s -= scope.popleft()[1]

        answer = max(answer, s)

    print(answer)


if __name__ == "__main__":
    main()
