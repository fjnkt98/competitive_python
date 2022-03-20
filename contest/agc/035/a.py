from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    N: int = int(input())
    A: List[int] = list(map(int, input().split()))

    counter = collections.Counter(A)

    if len(counter) == 1:
        print("Yes" if counter[0] == N else "No")
    elif len(counter) == 2:
        print("Yes" if counter[0] == N // 3 else "No")
    elif len(counter) == 3:
        x, y, z = counter.keys()
        if (
            x ^ y ^ z == 0
            and counter[x] == N // 3
            and counter[y] == N // 3
            and counter[z] == N // 3
        ):
            print("Yes")
        else:
            print("No")
    else:
        print("No")


if __name__ == "__main__":
    main()
