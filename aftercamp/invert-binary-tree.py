# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root

        ans = TreeNode()
        dummy = ans
        def dfs(root, dummy):
            if not root:
                return

            dummy.val = root.val
            if root.right:
                dummy.left = TreeNode()
                dfs(root.right, dummy.left)
            if root.left:
                dummy.right = TreeNode()
                dfs(root.left, dummy.right)

        dfs(root, dummy)
        
        return ans