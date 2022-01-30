from typing import List, Tuple, Union


class Node:
    def __init__(self, key: int):
        self.key: int = key
        self.previous_node: Node = None
        self.next_node: Node = None


class DoublyLinkedList:
    def __init__(self):
        self.nil: Node = Node(None)
        self.nil.previous_node = self.nil
        self.nil.next_node = self.nil

    def insert(self, key: int):
        new_node = Node(key)
        new_node.next_node = self.nil.next_node
        self.nil.next_node.previous_node = new_node
        self.nil.next_node = new_node
        new_node.previous_node = self.nil

    def search(self, key: int) -> Node:
        current_node: Node = self.nil.next_node
        while current_node != self.nil and current_node.key != key:
            current_node = current_node.next_node

        return current_node

    def delete(self, t: Node):
        if t == self.nil:
            return

        t.previous_node.next_node = t.next_node
        t.next_node.previous_node = t.previous_node

    def delete_first(self):
        self.delete(self.nil.next_node)

    def delete_last(self):
        self.delete(self.nil.previous_node)

    def delete_by_key(self, key: int):
        self.delete(self.search(key))

    def print(self):
        current_node: Node = self.nil.next_node
        result: List[int] = []

        while current_node != self.nil:
            result.append(current_node.key)
            current_node = current_node.next_node

        print(" ".join(map(str, result)))


def main():
    N = int(input())
    S: List[str] = [input() for i in range(N)]

    list: DoublyLinkedList = DoublyLinkedList()

    for s in S:
        c: List[str] = s.split()
        command: str = c[0]
        if command != "deleteFirst" and command != "deleteLast":
            value: int = int(c[1])

        if command == "insert":
            list.insert(value)
        elif command == "delete":
            list.delete_by_key(value)
        elif command == "deleteFirst":
            list.delete_first()
        elif command == "deleteLast":
            list.delete_last()

    list.print()


if __name__ == "__main__":
    main()
