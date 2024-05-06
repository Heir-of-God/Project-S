# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList(head):
            temp = None
            while head:
                t = head.next
                head.next = temp
                temp = head
                head = t

            return temp

        head = reverseList(head)

        cur_max = head.val
        cur_node = head.next
        last = head
        while cur_node:
            if cur_node.val < cur_max:
                last.next = cur_node.next
            else:
                cur_max = cur_node.val
                last = cur_node

            cur_node = cur_node.next

        head = reverseList(head)
        return head
