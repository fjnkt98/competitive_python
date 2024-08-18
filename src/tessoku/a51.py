def main() -> None:
    Q: int = int(input())

    D = []

    for _ in range(Q):
        line = input().split()
        if line[0] == "1":
            D.append(line[1])
        elif line[0] == "2":
            print(D[-1])
        else:
            D.pop()


if __name__ == "__main__":
    main()
