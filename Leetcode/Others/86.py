# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode()
        to_connect_less = dummy1
        dummy2 = ListNode()
        to_connect_greater = dummy2

        while head:
            nxt = head.next
            if head.val < x:
                to_connect_less.next = head
                to_connect_less = to_connect_less.next
            else:
                to_connect_greater.next = head
                to_connect_greater = to_connect_greater.next
            head.next = None
            head = nxt

        to_connect_less.next = dummy2.next
        return dummy1.next
