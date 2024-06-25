class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        cur_val_add: int = 0

        def recursion(node) -> None:
            nonlocal cur_val_add
            if not node:
                return
            recursion(node.right)
            cur_val_add += node.val
            node.val = cur_val_add
            recursion(node.left)

        recursion(root)
        return root


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        cur_val_add: int = 0
        mid_node: TreeNode = root
        queue: list[TreeNode] = []

        while queue or mid_node:
            while mid_node is not None:
                queue.append(mid_node)
                mid_node = mid_node.right
            mid_node = queue.pop()
            cur_val_add += mid_node.val
            mid_node.val = cur_val_add
            mid_node = mid_node.left

        return root
