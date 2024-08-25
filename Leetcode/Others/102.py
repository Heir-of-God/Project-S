# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res: list[list[int]] = []
        queue: list[TreeNode] = [root]

        while queue:
            res.append([])
            nxt_q: list[TreeNode] = []

            for node in queue:
                res[-1].append(node.val)
                if node.left:
                    nxt_q.append(node.left)
                if node.right:
                    nxt_q.append(node.right)

            queue = nxt_q

        return res
