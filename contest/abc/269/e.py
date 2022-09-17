from typing import *
import collections
import itertools
import bisect
import math


def main():
    N: int = int(input())

    left: int = 1
    right: int = N
    while right - left > 0:
        mid: int = (right + left) // 2
        print(f"? {left} {mid} 1 {N}", flush=True)
        T: int = int(input())
        if T == -1:
            raise ValueError

        if left == mid and T == 0:
            right = mid
            break

        if T == (mid - left + 1):
            left = mid + 1
        else:
            right = mid

    R: int = right

    left = 1
    right = N
    while right - left > 0:
        mid: int = (right + left) // 2
        print(f"? 1 {N} {left} {mid}", flush=True)
        T: int = int(input())
        if T == -1:
            raise ValueError

        if left == mid and T == 0:
            right = mid
            break

        if T == (mid - left + 1):
            left = mid + 1
        else:
            right = mid

    C: int = right

    print(f"! {R} {C}", flush=True)
    exit()


if __name__ == "__main__":
    main()
