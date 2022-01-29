from typing import List


def insertion_sort(A: List[int], N: int):
    for i in range(1, N):
        v: int = A[i]

        j: int = i - 1

        print(" ".join(map(str, A)))

        while j >= 0 and A[j] > v:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = v


def main():
    N = int(input())
    A = list(map(int, input().split()))

    insertion_sort(A, N)

    print(" ".join(map(str, A)))


if __name__ == "__main__":
    main()
