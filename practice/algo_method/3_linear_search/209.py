def main():
    N, V = map(int, input().split())
    A = list(map(int, input().split()))

    if V in A:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
