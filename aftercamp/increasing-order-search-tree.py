# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorderTraversal(root):
            if not root:
                return []

            arr = inorderTraversal(root.left)
            arr += [root.val]
            arr += inorderTraversal(root.right)

            return arr

        arr = inorderTraversal(root)
        ans = TreeNode()
        dummy = ans
        dummy.val = arr[0]
        for idx in range(1, len(arr)):
            dummy.right = TreeNode()
            dummy = dummy.right
            dummy.val = arr[idx]

        return ans

        