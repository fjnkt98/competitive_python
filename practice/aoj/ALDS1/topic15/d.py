from typing import List, Tuple, Counter, Union, Dict
import sys
import collections
import heapq
from array import array


sys.setrecursionlimit(1000000)
input = sys.stdin.readline


class HuffmanNode:
    def __init__(self, v: int, label: str = ""):
        self.value: int = v
        self.label: str = label
        self.left_child: Union[HuffmanNode, None] = None
        self.right_child: Union[HuffmanNode, None] = None
        # self.parent: Union[HuffmanNode, None] = None

    def __lt__(self, other):
        if not isinstance(other, HuffmanNode):
            return NotImplemented

        # return self.value < other.value

        if self.value == other.value:
            return self.label < other.label
        else:
            return self.value < other.value


def dfs(node: HuffmanNode, bit_assign: Dict[str, str], current_bit: str):
    if node.label != "":
        bit_assign[node.label] = current_bit

    if node.left_child is not None:
        dfs(node.left_child, bit_assign, current_bit + "0")

    if node.right_child is not None:
        dfs(node.right_child, bit_assign, current_bit + "1")


def main():
    S: str = input()
    count: Counter[str] = Counter(S)

    if len(count) == 2:
        print(len(S) - 1)
        return

    nodes: List[HuffmanNode] = [
        HuffmanNode(value, label) for (label, value) in count.items()
    ]
    nodes.pop()

    heapq.heapify(nodes)
    while len(nodes) != 1:
        x: HuffmanNode = heapq.heappop(nodes)
        y: HuffmanNode = heapq.heappop(nodes)

        z = HuffmanNode(x.value + y.value)
        if x.label == "":
            z.left_child = y
            z.right_child = x
        else:
            z.left_child = x
            z.right_child = y

        heapq.heappush(nodes, z)

    bit_assign: Dict[str, str] = {}
    dfs(nodes[0], bit_assign, "")

    answer: List[str] = []
    for s in S:
        if s != "\n":
            answer.append(bit_assign[s])

    # print("".join(answer))
    print(len("".join(answer)))


if __name__ == "__main__":
    main()
