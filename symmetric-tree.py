# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        if p == None and q == None:
            return True

        if not p or not q:
            return False

        if p and q and p.val != q.val:
            return False

        return self.isSameTree(p.right, q.left) and self.isSameTree(p.left, q.right)
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = root.left
        right = root.right

        return self.isSameTree(left, right)