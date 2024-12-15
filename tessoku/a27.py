import math


def main() -> None:
    A, B = map(int, input().split())

    print(math.gcd(A, B))


if __name__ == "__main__":
    main()
