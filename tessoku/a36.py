def main() -> None:
    N, K = map(int, input().split())

    C = 2 * (N - 1)
    R = K - C
    if R < 0:
        print("No")
        return

    if R % 2 == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
