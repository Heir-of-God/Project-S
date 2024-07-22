class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(next=head)
        to_connect = dummy
        cur = head

        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next

            if to_connect.next == cur:
                to_connect = cur
                cur = cur.next

            else:
                to_connect.next = cur.next
                cur = cur.next

        return dummy.next
