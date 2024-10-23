# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [(root, None)]
        root.val = 0

        while stack:
            sum_whole = 0
            parent_sums = {}
            nxt = []

            for node, parent in stack:
                if node.left:
                    nxt.append((node.left, node))
                if node.right:
                    nxt.append((node.right, node))
                sum_whole += node.val
                if not parent in parent_sums:
                    parent_sums[parent] = 0
                parent_sums[parent] += node.val

            for ind in range(len(stack)):
                stack[ind][0].val = sum_whole - parent_sums[stack[ind][1]]

            stack = nxt

        return root
