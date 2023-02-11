# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = []
        dummy = ListNode()
        dummy.next = head
        curr = head
        prev = dummy
        value = -101

        while curr:
            if curr.val == value and value not in seen:
                seen.append(value)
            value = curr.val
            curr = curr.next

        curr = head
        while curr:
            if curr.val in seen:
                prev.next = prev.next.next
            else:
                prev = prev.next
            curr = curr.next

        return dummy.next
