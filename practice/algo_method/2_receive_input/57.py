def main():
    N = int(input())
    A = list(map(int, input().split()))

    for a in reversed(A):
        print(a)


if __name__ == "__main__":
    main()
