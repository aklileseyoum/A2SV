# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        o = odd
        even = ListNode()
        e = even
        even_no = 0
        odd_no = 0

        while head:
            if even_no == 0 and odd_no == 0:
                o.next = head
                o = o.next
                odd_no = 1
            elif even_no == 1 and odd_no == 0:
                o.next = head
                o = o.next
                odd_no = 1
                even_no = 0
            elif even_no == 0 and odd_no == 1:
                e.next = head
                e = e.next
                odd_no = 0
                even_no = 1
            head = head.next

        e.next = None
        o.next = even.next
        return odd.next
