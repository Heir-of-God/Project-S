# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def recursion(cur_node):
            if cur_node is None:
                return

            recursion(cur_node.left)
            recursion(cur_node.right)
            res.append(cur_node.val)

            return

        recursion(root)
        return res
