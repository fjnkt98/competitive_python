from typing import *
import itertools


def main():
    S: str = input()

    D: Dict[int, int] = {
        0: 3,
        1: 2,
        2: 4,
        3: 1,
        4: 3,
        5: 5,
        6: 0,
        7: 2,
        8: 4,
        9: 6,
    }

    C: List[int] = [0] * 7
    for i, s in enumerate(S):
        if s == "1":
            C[D[i]] += 1

    ok: bool = False
    for i, j in itertools.combinations(range(7), r=2):
        flag2: bool = False
        if C[i] >= 1 and C[j] >= 1:
            for k in range(i + 1, j):
                if C[k] == 0:
                    ok = True

    if ok and S[0] == "0":
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
