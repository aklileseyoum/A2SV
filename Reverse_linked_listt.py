# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        counter = 0
        cur = head
        left_end = None
        right_end = None
        before_left = None
        before_right = None
        prev = None

        while cur:
            counter += 1
            if counter == left:
                left_end = cur
                before_left = prev
            if counter == right:
                right_end = cur
                break

            prev = cur
            cur = cur.next
        
        after_right = cur.next
        curr = left_end
        prevv = None

        while curr != after_right:
            temp = curr.next
            curr.next = prevv
            prevv = curr
            curr = temp
     
        if before_left:
            before_left.next = prevv
        else:
            dummy.next = prevv

        cur = prevv
        while cur.next:
            cur = cur.next
        cur.next = after_right
        
        return dummy.next
