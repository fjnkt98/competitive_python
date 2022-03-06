from typing import List, Tuple
import sys
from array import array
import numpy as np


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    cx, cy = map(int, input().split())

    ba = np.array([ax - bx, ay - by, 0])
    bc = np.array([cx - bx, cy - by, 0])

    ca = np.array([ax - cx, ay - cy, 0])
    cb = np.array([bx - cx, by - cy, 0])

    answer: float = 0.0
    if ba @ bc < 0:
        answer = np.linalg.norm(ba)
    elif ca @ cb < 0:
        answer = np.linalg.norm(ca)
    else:
        answer = np.abs(np.linalg.norm(np.cross(ba, bc))) / np.linalg.norm(cb)

    print(answer)


if __name__ == "__main__":
    main()
