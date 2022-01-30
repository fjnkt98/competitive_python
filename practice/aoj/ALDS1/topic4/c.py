from typing import List, DefaultDict
import collections


def main():
    N = int(input())

    d: DefaultDict[str, int] = collections.defaultdict(int)
    for i in range(N):
        command, key = input().split()

        if command == "insert":
            d[key] += 1
        elif command == "find":
            if d[key] == 0:
                print("no")
            else:
                print("yes")


if __name__ == "__main__":
    main()
