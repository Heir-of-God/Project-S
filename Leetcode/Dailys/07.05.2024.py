# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList(head):
            temp = None
            while head:
                t = head.next
                head.next = temp
                temp = head
                head = t

            return temp

        head = reverseList(head)
        first_head = head
        cur_add = 0

        while True:
            new_num = (head.val * 2) + cur_add
            new_dig_here = new_num % 10
            cur_add = new_num // 10
            head.val = new_dig_here
            if head.next is None:
                break
            head = head.next

        if cur_add != 0:
            head.next = ListNode(val=cur_add, next=None)

        return reverseList(first_head)
