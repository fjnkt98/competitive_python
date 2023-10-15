def main() -> None:
    _: int = int(input())
    S: str = input().rstrip()

    if "RRR" in S or "BBB" in S:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
