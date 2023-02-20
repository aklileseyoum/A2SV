# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        addition = ListNode()
        curr = addition
        
        first = l1
        second = l2
        carry = 0
        while first and second:
            value = first.val + second.val + carry
            if value < 10:
                curr.val = value
                carry = 0
            else:
                curr.val = value % 10
                carry = value // 10
            new_node = ListNode()
            curr.next = new_node
            curr = curr.next
            first = first.next
            second = second.next

        if first != None:
            while first:
                value = first.val + carry
                if value < 10:
                    curr.val = value
                    carry = 0
                else:
                    curr.val = value % 10
                    carry = value // 10
                new_node = ListNode()
                curr.next = new_node
                curr = curr.next
                first = first.next

        if second != None:
            while second:
                value = second.val + carry
                if value < 10:
                    curr.val = value
                    carry = 0
                else:
                    curr.val = value % 10
                    carry = value // 10
                new_node = ListNode()
                curr.next = new_node
                curr = curr.next
                second = second.next

        if carry != 0:
            curr.val = carry
        else:
            cur = addition
            while cur.next.next:
                cur = cur.next
            cur.next = None

        return addition
