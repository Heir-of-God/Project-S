class Solution:
    def modifiedList(self, nums: list[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode()
        connect = dummy

        while head:
            nxt = head.next
            if head.val not in nums:
                head.next = None
                connect.next = head
                connect = connect.next
            head = nxt

        return dummy.next
