# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortoise = head
        rabbit = head
        answer = "no cycle"
        found = 0
        while rabbit and rabbit.next:
            tortoise = tortoise.next
            rabbit = rabbit.next.next
            if rabbit == tortoise:
                found = 1
                break

        if found == 1:
            tortoise = head
            while rabbit and tortoise:
                if rabbit == tortoise:
                    return rabbit
                rabbit = rabbit.next
                tortoise = tortoise.next
