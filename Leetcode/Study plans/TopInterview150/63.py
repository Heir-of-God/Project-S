class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev_delete = dummy
        to_end = prev_delete

        for _ in range(n + 1):
            to_end = to_end.next

        while to_end != None:
            to_end = to_end.next
            prev_delete = prev_delete.next

        prev_delete.next = prev_delete.next.next
        return dummy.next
