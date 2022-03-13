from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, X = map(int, input().split())
    S = input().rstrip()

    T: List[str] = []
    i: int = 0
    move_to_child: int = 0
    while i < N:
        if S[i] == "U":
            if move_to_child > 0:
                T.pop()
                move_to_child = max(0, move_to_child - 1)
            else:
                T.append(S[i])

        else:
            T.append(S[i])
            move_to_child += 1
        i += 1

    for s in T:
        if s == "U":
            X = X // 2
        elif s == "L":
            X = 2 * X
        elif s == "R":
            X = 2 * X + 1

    print(X)


if __name__ == "__main__":
    main()
