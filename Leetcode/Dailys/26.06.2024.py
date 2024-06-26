class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes: list[TreeNode] = []

        def recursion(node) -> None:
            nonlocal nodes
            if node is None:
                return
            recursion(node.left)
            nodes.append(node.val)
            recursion(node.right)

        recursion(root)

        def create_balanced_tree(range_start, range_end) -> TreeNode | None:
            if range_start > range_end:
                return None
            mid: int = (range_start + range_end) // 2
            left: TreeNode | None = create_balanced_tree(range_start, mid - 1)
            right: TreeNode | None = create_balanced_tree(mid + 1, range_end)

            node = TreeNode(nodes[mid], left, right)
            return node

        return create_balanced_tree(0, len(nodes) - 1)
