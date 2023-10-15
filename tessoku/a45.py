def convert(c: str) -> int:
    match c:
        case "W":
            return 0
        case "R":
            return 1
        case "B":
            return 2


def main() -> None:
    N, C = input().split()
    N = int(N)
    A = list(input())

    B = [convert(a) for a in A]
    c = convert(C)

    if sum(B) % 3 == c:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
