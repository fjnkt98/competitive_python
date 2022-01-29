from typing import List, Tuple


def bubble_sort(A: List[Tuple[int, str]], N: int):
    flag: bool = True

    count: int = 0
    while flag:
        flag = False
        for i in range(N - 1, 0, -1):
            if A[i][0] < A[i - 1][0]:
                A[i], A[i - 1] = A[i - 1], A[i]
                count += 1
                flag = True


def selection_sort(A: List[Tuple[int, str]], N: int):
    count: int = 0
    for i in range(N):
        minimum_j: int = i

        for j in range(i, N):
            if A[j][0] < A[minimum_j][0]:
                minimum_j = j
        if A[i][0] != A[minimum_j][0]:
            count += 1
        A[i], A[minimum_j] = A[minimum_j], A[i]


def main():
    N = int(input())
    A: List[str] = input().split()

    B = [(s[1], s[0]) for s in A]
    C = [(s[1], s[0]) for s in A]

    bubble_sort(B, N)
    print(" ".join(map(lambda t: str(t[1]) + str(t[0]), B)))
    print("Stable")
    selection_sort(C, N)
    print(" ".join(map(lambda t: str(t[1]) + str(t[0]), C)))
    if C == B:
        print("Stable")
    else:
        print("Not stable")


if __name__ == "__main__":
    main()
