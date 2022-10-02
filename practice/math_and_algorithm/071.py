from typing import *
import collections
import itertools
import bisect
import math
import numpy as np


def main():
    N: int = int(input())
    M: np.ndarray = np.array(
        [list(map(int, input().split())) for i in range(N)], dtype=np.float64
    )

    n: int = N + 2
    m: int = N

    A: np.ndarray = np.zeros((m, n), dtype=np.float64)
    A[:, : (n - m)] = M[:, : (n - m)]
    A[:, (n - m) :] = np.eye(m)
    b: np.ndarray = M[:, 2]

    c: np.ndarray = np.array([0 for i in range(n)], dtype=np.float64)
    c[0] = 1
    c[1] = 1

    basis_indices: List[int] = list(range(2, m + 2))
    non_basis_indices: List[int] = list(range(2))

    N: np.ndarray = A[:, non_basis_indices]
    B: np.ndarray = A[:, basis_indices]
    cn: np.ndarray = c[non_basis_indices]
    cb: np.ndarray = c[basis_indices]
    x: np.ndarray = np.zeros(n)
    x[basis_indices] = b.copy()

    xb: np.ndarray = x[basis_indices]
    while True:
        # step. 2 被約費用の計算
        b_bar: np.ndarray = np.dot(np.linalg.inv(B), b)
        c_bar: np.ndarray = cn - np.dot(N.T, np.dot(np.linalg.inv(B).T, cb))

        # step. 3
        # これ以上最適化できなくなったら終了
        if (c_bar <= 0).all():
            print("Stop")
            break

        # step.4
        # 被約費用が正かつ最小の添字kを取得する
        k = np.where(c_bar > 0)[0][0]
        N_bar: np.ndarray = np.dot(np.linalg.inv(B), N)
        # ベクトルaを取得する
        a_bar: np.ndarray = N_bar[:, k]

        if (a_bar <= 0).all():
            print("Non bound")
            break

        T: np.ndarray = np.where(a_bar > 0, b_bar / a_bar, np.inf)
        theta: float = np.min(T)
        i: int = np.argmin(T)

        # step. 5
        x[non_basis_indices[k]] = theta
        xb = (b_bar - theta * a_bar).copy()
        basis_indices[i], non_basis_indices[k] = non_basis_indices[k], basis_indices[i]

        tmp: np.ndarray = N[:, k].copy()
        N[:, k] = B[:, i]
        B[:, i] = tmp

        tmp = cn[k]
        cn[k] = cb[i]
        cb[i] = tmp

    for i in range(m):
        print(basis_indices[i], xb[i])

    print(xb)


if __name__ == "__main__":
    main()
