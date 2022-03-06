from typing import List, Tuple
import sys
from array import array
import numpy as np


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    A, B, H, M = map(int, input().split())
    theta_m: float = np.pi * M / 30
    theta_h: float = np.pi * H / 6 + theta_m / 12

    b = np.array([B * np.sin(theta_m), B * np.cos(theta_m)])
    a = np.array([A * np.sin(theta_h), A * np.cos(theta_h)])

    ab = b - a

    print(np.linalg.norm(ab))


if __name__ == "__main__":
    main()
