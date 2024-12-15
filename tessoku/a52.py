from collections import deque


def main() -> None:
    Q: int = int(input())
    D = deque()

    for _ in range(Q):
        line = input().split()
        if line[0] == "1":
            D.append(line[1])
        elif line[0] == "2":
            print(D[0])
        else:
            D.popleft()


if __name__ == "__main__":
    main()
