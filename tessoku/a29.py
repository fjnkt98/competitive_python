def main() -> None:
    a, b = map(int, input().split())

    print(pow(a, b, 1000000007))


if __name__ == "__main__":
    main()
