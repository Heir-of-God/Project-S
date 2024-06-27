# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def recursion(node, parent, grandparent):
            if node is None:
                return 0
            local_res = 0
            local_res += recursion(node.left, node, parent)
            local_res += recursion(node.right, node, parent)
            if grandparent.val & 1 == 0:
                local_res += node.val
            return local_res

        res = 0
        if root.left:
            res += recursion(root.left.left, root.left, root)
            res += recursion(root.left.right, root.left, root)
        if root.right:
            res += recursion(root.right.right, root.right, root)
            res += recursion(root.right.left, root.right, root)

        return res


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        queue: list[TreeNode] = [root]

        while queue:
            cur_node = queue.pop()
            if cur_node.val & 1 == 0:
                if cur_node.left:
                    res += cur_node.left.left.val if cur_node.left.left else 0
                    res += cur_node.left.right.val if cur_node.left.right else 0
                if cur_node.right:
                    res += cur_node.right.left.val if cur_node.right.left else 0
                    res += cur_node.right.right.val if cur_node.right.right else 0

            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)

        return res
