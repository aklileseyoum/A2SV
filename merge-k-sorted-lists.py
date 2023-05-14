# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        save = []
        for idx in range(len(lists)):
            if lists[idx]:
                save.append([lists[idx].val, idx])
        
        heapify(save)
        answer = ListNode()
        ans = answer
        while save:
            val = heappop(save)
            new = ListNode(val[0])
            ans.next = new
            ans = ans.next
            lists[val[1]] = lists[val[1]].next
            if lists[val[1]]:
                heappush(save, [lists[val[1]].val, val[1]])

        return answer.next