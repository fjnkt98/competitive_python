import sys

sys.setrecursionlimit(1000000)


def main() -> None:
    S = input()
    index = S.rfind("a")
    print(-1 if index == -1 else index + 1)


if __name__ == "__main__":
    main()
