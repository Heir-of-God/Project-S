# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy = ListNode(next=head)
        just_before_range = dummy
        for _ in range(left - 1):
            just_before_range = just_before_range.next

        cur_node = just_before_range.next
        first_in_range = cur_node
        prev_reversed = None

        for _ in range(right - left + 1):
            nxt = cur_node.next
            just_before_range.next = cur_node
            cur_node.next = prev_reversed
            prev_reversed = cur_node
            cur_node = nxt

        first_in_range.next = cur_node

        return dummy.next
