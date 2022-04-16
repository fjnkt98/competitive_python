from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)


def main():
    N: int = int(input())
    S: List[str] = [""] * N
    T: List[str] = [""] * N
    for i in range(N):
        S[i], T[i] = input().split()

    for i, (s, t) in enumerate(zip(S, T)):
        ok: bool = False

        s_is_ok: bool = True
        for j, (u, v) in enumerate(zip(S, T)):
            if i == j:
                continue
            if s == u or s == v:
                s_is_ok = False

        t_is_ok: bool = True
        for j, (u, v) in enumerate(zip(S, T)):
            if i == j:
                continue
            if t == u or t == v:
                t_is_ok = False

        ok = s_is_ok | t_is_ok

        if not ok:
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    main()
