from typing import *
import collections
import itertools
import bisect
import math


def main():
    S: str = input()

    D: Dict[str, int] = {
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
    }

    print(6 - D[S])


if __name__ == "__main__":
    main()
