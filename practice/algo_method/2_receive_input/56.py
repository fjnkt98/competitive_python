def main():
    N = int(input())
    A = list(map(int, input().split()))

    for a in A:
        if a % 3 == 0:
            print(a)


if __name__ == "__main__":
    main()
