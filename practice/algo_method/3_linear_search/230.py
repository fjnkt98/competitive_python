def main():
    N = int(input())
    S = input()
    T = input()

    count: int = 0
    for i in range(N):
        if S[i] != T[i]:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
