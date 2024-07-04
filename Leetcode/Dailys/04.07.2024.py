from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_node = head.next

        while cur_node is not None:
            if cur_node.next.val != 0:
                cur_node.val += cur_node.next.val
                cur_node.next = cur_node.next.next
            else:
                cur_node.next = cur_node.next.next
                cur_node = cur_node.next

        return head.next
