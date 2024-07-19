# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        cur = head
        while cur is not None:
            cur = cur.next
            length += 1

        res = [None for _ in range(k)]
        if length == 0:
            return res

        every_part_min_size = length // k
        additional_parts = length - (every_part_min_size * k)

        cur_node = head
        for part_ind in range(k):
            res[part_ind] = cur_node

            to_end = every_part_min_size + (additional_parts > 0)
            additional_parts -= additional_parts > 0

            for _ in range(to_end):
                prev = cur_node
                cur_node = cur_node.next

            if prev:
                prev.next = None

        return res
