from typing import List, Tuple, Set
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)


def main():
    N: int = int(input())
    W: List[str] = [input() for i in range(N)]

    used: Set[str] = set()
    used.add(W[0])
    prev_word: str = W[0]
    ok: bool = True
    for w in W[1:]:
        if w in used:
            ok = False
            break

        if prev_word[-1] != w[0]:
            ok = False
            break

        used.add(w)
        prev_word = w

    print("Yes" if ok else "No")


if __name__ == "__main__":
    main()
