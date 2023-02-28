# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        tail = dummy
        def merge(first, second):
            tail = None
            if not first:
                return second
            elif not second:
                return first
            
            if first.val > second.val:
                tail = second
                tail.next = merge(first, second.next)
            else:
                tail = first
                tail.next = merge(first.next, second)
            
            return tail

        return merge(list1, list2)
