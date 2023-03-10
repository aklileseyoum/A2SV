# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return 
        q = deque([root])
        ans = []
        print(q)
        while q:
            ans.append([i.val for i in q])
            for i in range(len(q)):
                node = q.popleft()
                if node and node.left:
                   q.append(node.left)
                if node and node.right:    
                    q.append(node.right)
        return ans