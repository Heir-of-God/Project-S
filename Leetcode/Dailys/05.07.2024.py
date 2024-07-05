from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        res = [-1, -1]
        prev_critical_ind = None
        first_critical_ind = None
        prev = head
        cur = head.next
        cur_ind = 1

        while cur.next:
            if (cur.val > prev.val and cur.val > cur.next.val) or (cur.val < prev.val and cur.val < cur.next.val):
                if prev_critical_ind is not None:
                    res[0] = min(res[0], cur_ind - prev_critical_ind) if res[0] != -1 else cur_ind - prev_critical_ind
                else:
                    first_critical_ind = cur_ind
                prev_critical_ind = cur_ind

            prev = cur
            cur = cur.next
            cur_ind += 1

        if prev_critical_ind != first_critical_ind:
            res[1] = prev_critical_ind - first_critical_ind

        return res
