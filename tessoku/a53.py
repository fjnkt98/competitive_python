import heapq


def main() -> None:
    Q: int = int(input())
    A = []

    for _ in range(Q):
        line = input().split()

        if line[0] == "1":
            heapq.heappush(A, int(line[1]))
        elif line[0] == "2":
            print(A[0])
        else:
            heapq.heappop(A)


if __name__ == "__main__":
    main()
