# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode()
        connect = dummy
        cur = head

        while cur and cur.next:
            nxt = cur.next.next
            connect.next = cur.next
            connect = connect.next
            connect.next = cur
            connect = connect.next
            cur = nxt

        connect.next = cur

        return dummy.next
