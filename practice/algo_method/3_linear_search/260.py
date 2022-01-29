from typing import List


def main():
    N = int(input())
    S: List[str] = [input() for i in range(N)]

    if len(S) != len(set(S)):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
