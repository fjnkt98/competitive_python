from typing import List, Tuple
import sys
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N, A, B, C, D = map(int, input().split())
    S: str = input().rstrip()

    ok: bool = True
    if C < D:
        if "##" in S[min(A, B) - 1 : max(C, D)]:
            ok = False
    else:
        if "##" in S[min(A, B) - 1 : max(C, D)]:
            ok = False
        if "..." not in S[B - 2 : D + 1]:
            ok = False

    print("Yes" if ok else "No")


if __name__ == "__main__":
    main()
