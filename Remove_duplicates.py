# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = []
        curr = head
        prev = curr
        while curr:
            if curr.val in seen:
                prev.next = curr.next
            else:
                seen.append(curr.val)
                prev = curr
            curr = curr.next

        return head
