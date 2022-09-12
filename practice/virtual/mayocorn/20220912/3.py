from typing import *
import collections
import itertools
import bisect
import math


def main():
    S: str = input()
    T: str = input()

    SS: List[Tuple[str, int]] = [(k, len(list(v))) for k, v in itertools.groupby(S)]
    TT: List[Tuple[str, int]] = [(k, len(list(v))) for k, v in itertools.groupby(T)]

    if len(SS) != len(TT):
        print("No")
        return

    ok: bool = True
    for s, t in zip(SS, TT):
        if s[0] != t[0]:
            ok = False

        if s[1] == 1:
            if t[1] != 1:
                ok = False
        else:
            if s[1] > t[1]:
                ok = False

    print("Yes" if ok else "No")


if __name__ == "__main__":
    main()
