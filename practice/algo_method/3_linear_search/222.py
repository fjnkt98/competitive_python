def main():
    N = int(input())

    if N == 1:
        print("No")
        return

    is_prime: bool = True
    for i in range(2, N):
        if N % i == 0:
            is_prime = False

    if is_prime:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
