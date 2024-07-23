# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        to_connect_less = dummy
        first_node_greater_equal = None
        last_node_greater_equal = None

        cur = head
        while cur:
            nxt = cur.next
            if cur.val < x:
                to_connect_less.next = cur
                to_connect_less = to_connect_less.next
                if first_node_greater_equal is not None:
                    last_node_greater_equal.next = nxt
                cur.next = None
            else:
                if first_node_greater_equal is None:
                    first_node_greater_equal = cur
                last_node_greater_equal = cur
            cur = nxt

        to_connect_less.next = first_node_greater_equal

        return dummy.next
