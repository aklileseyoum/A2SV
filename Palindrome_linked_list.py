# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode()
        dummy.next = head
        new = dummy
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = None
        prevv = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prevv
            prevv = curr
            curr = temp

        new.next= prevv

        compare = new.next
        
        if fast:
            slow = slow.next

        while compare and slow:
            if compare.val != slow.val:
                return False
            compare = compare.next
            slow = slow.next

        return True
