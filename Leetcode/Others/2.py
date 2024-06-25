from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        add_from_previous = 0
        node1 = l1
        node2 = l2

        while node1:
            new_val = node2.val + node1.val + add_from_previous
            if new_val // 10 != 0:
                add_from_previous = 1
                new_val %= 10
            else:
                add_from_previous = 0
            node2.val = new_val
            node1 = node1.next
            if node1:
                if not node2.next:
                    node2.next = ListNode()
                node2 = node2.next

        while add_from_previous != 0:
            if not node2.next:
                node2.next = ListNode()
            node2 = node2.next
            new_val = node2.val + add_from_previous
            if new_val // 10 != 0:
                add_from_previous = 1
                new_val %= 10
            else:
                add_from_previous = 0
            node2.val = new_val

        return l2
