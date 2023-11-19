# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dummy = head
        visited = set()
        visited.add(dummy)
        while dummy and dummy.next:
            dummy = dummy.next
            if dummy in visited:
                return True
            visited.add(dummy)


        