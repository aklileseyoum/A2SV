# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-5001)
        curr = head
        dummy.next = head
        sortedList = dummy
        curr = curr.next
        sortedList = sortedList.next
        sortedList.next = None

        while curr:
            sortedList = dummy
            prev = sortedList
            found = 0
            while sortedList:
                if sortedList.val > curr.val:
                    found = 1
                    break
                prev = sortedList
                sortedList = sortedList.next

            new_node = ListNode(curr.val)
            if found == 1:
                new_node.next = sortedList
            prev.next = new_node
            curr = curr.next

        return dummy.next
