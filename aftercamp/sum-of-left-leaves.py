# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, not_right):
            if not root:
                return

            if not root.left and not root.right and not_right:
                ans[-1] += root.val

            if root.left:
                dfs(root.left, True)
            if root.right:
                dfs(root.right, False)

        ans = [0]
        dfs(root, False)
        
        return ans[-1]