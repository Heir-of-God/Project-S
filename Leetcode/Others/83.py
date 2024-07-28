# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val="NOVALUE")
        to_connect = dummy

        while head:
            nxt = head.next
            head.next = None
            if to_connect.val != head.val:
                to_connect.next = head
                to_connect = to_connect.next
            head = nxt

        return dummy.next
