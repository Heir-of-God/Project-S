class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def preOrder(root: Node) -> None:
    res: list[int] = []

    def recursion(node: Node) -> None:
        res.append(node.info)
        if node.left:
            recursion(node.left)
        if node.right:
            recursion(node.right)

    recursion(root)
    print(*res)


def preOrder(root: Node) -> None:
    res: list[int] = []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.info)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    print(*res)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

preOrder(tree.root)
