from typing import *
import itertools
import random


def main():
    N: int = int(input())
    C: List[int] = [int(input()) for i in range(N)]

    A: List[Tuple[int, int]] = [(0, 0)]
    for i, c in enumerate(C):
        if i & 1 == 0:
            if A[-1][0] == c:
                _, n = A.pop()
                A.append((c, n + 1))
            else:
                A.append((c, 1))
        else:
            if A[-1][0] == c:
                _, n = A.pop()
                A.append((c, n + 1))
            else:
                num: int = 0
                while A and A[-1][0] != c:
                    _, n = A.pop()
                    num += n
                A.append((c, num + 1))

    A = list(itertools.chain(*[[c] * n for c, n in A]))
    print(A.count(0))


if __name__ == "__main__":
    main()
