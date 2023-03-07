# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True

        if not p and q:
            return False

        if not q and p:
            return False

        if p and q and p.val != q.val:
            return False

        result1 = self.isSameTree(p.left, q.left)
        result2 = self.isSameTree(p.right, q.right)
        answer = result1 and result2

        return answer