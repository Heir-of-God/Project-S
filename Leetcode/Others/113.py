# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        cur_path = []

        def recursion(cur_node, cur_sum):
            cur_path.append(cur_node.val)
            cur_sum += cur_node.val
            if not cur_node.left and not cur_node.right:
                if cur_sum == targetSum:
                    res.append(cur_path[:])
                cur_sum -= cur_node.val
                cur_path.pop()
                return

            if cur_node.left:
                recursion(cur_node.left, cur_sum)
            if cur_node.right:
                recursion(cur_node.right, cur_sum)
            cur_path.pop()
            return

        recursion(root, 0)
        return res


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        cur_path = []
        queue = [(root, False)]
        cur_sum = 0

        while queue:
            node, visited_children = queue.pop()
            if not visited_children:
                cur_sum += node.val
                cur_path.append(node.val)
                queue.append((node, True))
                if node.right:
                    queue.append((node.right, False))
                if node.left:
                    queue.append((node.left, False))
                if not node.left and not node.right and cur_sum == targetSum:
                    res.append(cur_path[:])
            else:
                cur_sum -= node.val
                cur_path.pop()

        return res
