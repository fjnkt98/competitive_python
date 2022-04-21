from typing import List, Tuple
import sys
import collections
import itertools


sys.setrecursionlimit(1000000)


def main():
    S: str = input()

    U: List[str] = []
    for t in S.replace("BC", "D").split("B"):
        U.extend(t.split("C"))

    answer: int = 0
    for u in list(filter(lambda s: s, U)):
        count: int = 0
        for c in u:
            if c == "A":
                count += 1
            else:
                answer += count

    print(answer)


if __name__ == "__main__":
    main()
