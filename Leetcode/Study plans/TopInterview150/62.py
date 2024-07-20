class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_group_end(cur_node):
            counter: int = k - 1
            while counter > 0 and cur_node.next:
                cur_node = cur_node.next
                counter -= 1
            return cur_node if counter == 0 else None

        def reverse_group(group_start: ListNode, group_end: ListNode):
            prev = None
            cur: ListNode = group_start
            new_group_start = group_end.next

            while cur != new_group_start:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

        dummy = ListNode()
        prev_group_end: ListNode = dummy

        while head:
            group_start = head
            group_end = get_group_end(head)
            if group_end is None:
                break
            next_group_start = group_end.next
            reverse_group(group_start, group_end)
            prev_group_end.next = group_end
            prev_group_end = group_start
            group_start.next = next_group_start
            head = next_group_start

        return dummy.next
