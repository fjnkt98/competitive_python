def main() -> None:
    Q: int = int(input())

    D = {}
    for _ in range(Q):
        line = input().split()
        match line[0]:
            case "1":
                x = line[1]
                y = line[2]
                D[x] = y
            case "2":
                x = line[1]
                print(D[x])


if __name__ == "__main__":
    main()
