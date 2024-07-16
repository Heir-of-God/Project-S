"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return head
        head_memo = head

        while head:
            head.next = Node(head.val, next=head.next)
            head = head.next.next

        head = head_memo
        while head and head.next:
            nxt = head.next.next
            clone = head.next
            clone.random = head.random.next if head.random is not None else None
            head = nxt

        res = head_memo.next
        cur = res

        while cur:
            cur.next = cur.next.next if cur.next else None
            cur = cur.next

        return res
