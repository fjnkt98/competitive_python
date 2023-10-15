def main() -> None:
    N, Q = map(int, input().split())
    flipped = False
    A = [i + 1 for i in range(N)]
    for _ in range(Q):
        values = input().split()
        if values[0] == "1":
            x = int(values[1]) - 1
            y = int(values[2])
            if flipped:
                x = N - x - 1
            A[x] = y
        elif values[0] == "2":
            flipped = not flipped
        else:
            x = int(values[1]) - 1
            if flipped:
                x = N - x - 1
            print(A[x])


if __name__ == "__main__":
    main()
