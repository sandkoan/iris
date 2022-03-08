from dataclasses import dataclass


class Node:
    pass


@dataclass
class ConstNode(Node):
    i: int


@dataclass
class NegNode(Node):
    node: Node


@dataclass
class AddNode(Node):
    left: Node
    right: Node


@dataclass
class MultNode(Node):
    left: Node
    right: Node


def evaluate(node: Node):
    match node:
        case ConstNode(i):
            return i
        case NegNode(n):
            return -evaluate(n)
        case AddNode(left, right):
            return evaluate(left) + evaluate(right)
        case MultNode(left, right):
            return evaluate(left) * evaluate(right)


if __name__ == '__main__':
    x: int = evaluate(
        AddNode(
            MultNode(
                ConstNode(10),
                NegNode(ConstNode(5))
            ),
            AddNode(
                ConstNode(77), ConstNode(10)
            )
        )
    )
    print(x)
