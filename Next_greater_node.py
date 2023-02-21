# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        answer = []
        curr = head
        while curr:
            answer.append(curr.val)
            curr = curr.next

        idx = len(answer) - 1
        seen = [0]
        while idx > -1:
            cur = answer[idx]
            if seen[-1] <= answer[idx]:
                if seen[-1] == 0:
                    answer[idx] = 0
                else:
                    while len(seen) > 0 and seen[-1] <= answer[idx]:
                        seen.pop()
                    if len(seen) > 0:
                        answer[idx] = seen[-1]
                    else:
                        answer[idx] = 0  
            else:
                answer[idx] = seen[-1]

            seen.append(cur)
            idx -= 1

        return answer
