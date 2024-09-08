class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        part_size: int = length // k
        extra: int = length - (part_size * k)
        res = []

        while head:
            res.append(head)
            for _ in range(part_size + (1 if extra else 0) - 1):
                head = head.next
            nxt = head.next
            head.next = None
            head = nxt
            if extra:
                extra -= 1

        while len(res) != k:
            res.append(None)

        return res
