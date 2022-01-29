from typing import List


def selection_sort(A: List[int], N: int):
    count: int = 0
    for i in range(N):
        minimum_j: int = i

        for j in range(i, N):
            if A[j] < A[minimum_j]:
                minimum_j = j
        if A[i] != A[minimum_j]:
            count += 1
        A[i], A[minimum_j] = A[minimum_j], A[i]

    print(" ".join(map(str, A)))
    print(count)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    selection_sort(A, N)


if __name__ == "__main__":
    main()
