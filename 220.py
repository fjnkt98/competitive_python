def main():
    N = int(input())

    count: int = 0
    for i in range(1, N + 1):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
