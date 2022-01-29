def main():
    L, R = map(int, input().split())

    count: int = 0
    for i in range(L, R + 1):
        S: str = str(i)
        if S == S[::-1]:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
