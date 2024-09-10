class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        cur = head
        while cur.next:
            nxt = cur.next
            val = gcd(cur.val, nxt.val)
            cur.next = ListNode(val=val, next=nxt)
            cur = nxt

        return head
