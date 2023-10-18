# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        while l1:
            num1 += l1.val
            num1 *= 10
            l1 = l1.next
        num1 //= 10
        num2 = 0
        while l2:
            num2 += l2.val
            num2 *= 10
            l2 = l2.next
        num2 //= 10
        ans = num1 + num2
        answer = ListNode()
        dummy = answer
        for idx in range(len(str(ans))):
            dummy.val = int(str(ans)[idx])
            if idx + 1 != len(str(ans)):
                dummy.next = ListNode()
                dummy = dummy.next

        return answer