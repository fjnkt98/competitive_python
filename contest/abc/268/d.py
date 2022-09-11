from typing import *
import collections
import itertools
import bisect
import math


def main():
    N, M = map(int, input().split())
    S: List[str] = [input() for i in range(N)]
    if M == 0:
        T: Set[str] = set()
    else:
        T: Set[str] = set([input() for i in range(M)])

    if N == 1:
        if 3 <= len(S[0]) <= 16 and (S[0] not in T):
            print(S[0])
        else:
            print(-1)
        return

    if N == 2:
        for x in range(1, 16 - len("".join(S)) + 1):
            A: str = ("_" * x).join([S[0], S[1]])
            B: str = ("_" * x).join([S[1], S[0]])
            if 3 <= len(A) <= 16 and (A not in T):
                print(A)
                return
            elif 3 <= len(B) <= 16 and (B not in T):
                print(B)
                return
        print(-1)
        return

    S.sort()
    for s in itertools.permutations(S):
        v: int = len("".join(s))
        for x in range(N - 1, 16 - v + 1):
            for splits in itertools.combinations(range(1, x), r=N - 2):
                A: List[str] = [s[0]]
                count: int = 0
                for i, b in enumerate(splits):
                    A.append("_" * (b - count))
                    count = b
                    A.append(s[i + 1])
                A.append("_" * (x - count))
                A.append(s[-1])

                X: str = "".join(A)
                if 3 <= len(X) <= 16 and (X not in T):
                    print(X)
                    return

    print(-1)


if __name__ == "__main__":
    main()
