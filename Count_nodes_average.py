# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averages(self,root):
        if root == None:
            return [0, 0, 0]

        right = self.averages(root.right)
        left = self.averages(root.left)
        summ = [root.val, 1, 0]
        summ[0] += right[0] + left[0]
        summ[1] += right[1] + left[1]
        summ[2] += right[2] + left[2]

        if summ[0] // summ[1] == root.val:
            summ[2] += 1

        return summ
        
    
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        return self.averages(root)[2]
        