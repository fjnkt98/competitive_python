def main():
    N, V = map(int, input().split())
    A = list(map(int, input().split()))

    print(A.count(V))


if __name__ == "__main__":
    main()
