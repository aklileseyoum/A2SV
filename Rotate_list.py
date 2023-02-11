# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 0
        count = head
        while count:
            size += 1
            count = count.next

        curr = head
        if size != 0:
            for i in range(k%size):
                curr = head

                if not curr or not curr.next:
                    break

                while curr.next:
                    prev = curr
                    curr = curr.next

                if prev:
                    prev.next = None
                new = head
                head = curr
                curr.next = new
        
        return curr
