# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# O(n) time and O(1) space
class Solution:
    def deleteNode(self, node) -> None:
        while node.next.next:
            node.val = node.next.val
            node = node.next
        node.val = node.next.val
        node.next = None


# O(1) time and O(1) space
class Solution:
    def deleteNode(self, node) -> None:
        node.val = node.next.val
        node.next = node.next.next
