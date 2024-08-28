# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def recursion(parent, isleft, cur_node):
            if cur_node.left:
                recursion(cur_node, True, cur_node.left)
            if cur_node.right:
                recursion(cur_node, False, cur_node.right)

            if (cur_node.left, cur_node.right) == (None, None) and cur_node.val == target:
                if isleft:
                    parent.left = None
                else:
                    parent.right = None

        dummy = TreeNode(left=root)
        recursion(dummy, True, root)

        return dummy.left
