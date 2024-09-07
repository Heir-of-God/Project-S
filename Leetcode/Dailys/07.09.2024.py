# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def recursion(cur_node_tree, cur_node_list):
            if cur_node_tree is None or cur_node_tree.val != cur_node_list.val:
                return False
            if cur_node_list.next is None:
                return True
            return recursion(cur_node_tree.left, cur_node_list.next) or recursion(
                cur_node_tree.right, cur_node_list.next
            )

        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == head.val and recursion(node, head) == True:
                return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return False
