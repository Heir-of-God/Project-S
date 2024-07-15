class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev_l1 = None
        res_head = l1

        add_from_previous = False
        while l1 or l2:
            cur_l1 = l1.val if l1 else 0
            cur_l2 = l2.val if l2 else 0

            local_res = cur_l1 + cur_l2 + add_from_previous
            here = local_res % 10
            add_from_previous = local_res // 10

            if l1 is None:
                prev_l1.next = ListNode(here)
                l1 = prev_l1.next
            else:
                l1.val = here
            prev_l1 = l1
            l1 = l1.next
            l2 = l2.next if l2 else None

        if add_from_previous:
            prev_l1.next = ListNode(1)

        return res_head
