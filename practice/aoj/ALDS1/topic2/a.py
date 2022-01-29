from typing import List


def bubble_sort(A: List[int], N: int):
    flag: bool = True

    count: int = 0
    while flag:
        flag = False
        for i in range(N - 1, 0, -1):
            if A[i] < A[i - 1]:
                A[i], A[i - 1] = A[i - 1], A[i]
                count += 1
                flag = True

    print(" ".join(map(str, A)))
    print(count)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    bubble_sort(A, N)


if __name__ == "__main__":
    main()
