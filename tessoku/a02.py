def main() -> None:
    N, X = map(int, input().split())
    A: list[int] = [int(v.strip()) for v in input().split()]

    if X in A:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
