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


# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
"""


def lca(root: Node, v1: int, v2: int) -> Node:
    def dfs_path(root: Node, trg: int) -> list[Node]:
        path: list[Node] = []
        queue: list[tuple[Node, bool]] = [(root, False)]

        while queue:
            node, visited_children = queue.pop()
            if not visited_children:
                path.append(node)
                if node.info == trg:
                    return path
                queue.append((node, True))
                if node.left:
                    queue.append((node.left, False))
                if node.right:
                    queue.append((node.right, False))
            else:
                path.pop()

        return []

    path1: list[Node] = dfs_path(root, v1)
    path2: list[Node] = dfs_path(root, v2)
    ind = 0
    while ind != min(len(path1), len(path2)) and path1[ind] is path2[ind]:
        ind += 1

    return path1[ind - 1]


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print(ans.info)
