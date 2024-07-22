# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        length = 1
        cur = head
        while cur.next:
            cur = cur.next
            length += 1
        k %= length
        if k == 0:
            return head
        cur.next = head

        cur = head
        for _ in range(length - k - 1):
            cur = cur.next
        new_head = cur.next
        cur.next = None

        return new_head
