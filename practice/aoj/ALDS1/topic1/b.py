from typing import List
import math


def main():
    x, y = map(int, input().split())

    print(math.gcd(x, y))


if __name__ == "__main__":
    main()
