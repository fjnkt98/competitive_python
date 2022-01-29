from typing import List, Deque
import collections


def main():
    S = input().split()

    stack: Deque[str] = collections.deque()
    answer: int = 0

    for s in S:
        if s == "+":
            op1: int = int(stack.pop())
            op2: int = int(stack.pop())
            stack.append(str(op2 + op1))
        elif s == "-":
            op1: int = int(stack.pop())
            op2: int = int(stack.pop())
            stack.append(str(op2 - op1))
        elif s == "*":
            op1: int = int(stack.pop())
            op2: int = int(stack.pop())
            stack.append(str(op2 * op1))
        else:
            stack.append(s)

    print(stack[0])


if __name__ == "__main__":
    main()
