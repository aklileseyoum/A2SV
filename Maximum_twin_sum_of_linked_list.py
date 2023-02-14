# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        listt = []
        curr = head
        while curr:
            listt.append(curr.val)
            curr = curr.next

        pt1 = 0
        pt2 = len(listt) - 1
        maximum = 0
        while pt1 < pt2:
            summ = listt[pt1] + listt[pt2]
            if summ > maximum:
                maximum = summ

            pt1 += 1
            pt2 -= 1
        
        return maximum
