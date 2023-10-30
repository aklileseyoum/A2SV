# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        delete = set(to_delete)
        res = set()
        res.add(root)
        def dfs(root):
            if not root:
                return 

            if root.val in delete:
                if root.left:
                    res.add(root.left)
                if root.right:
                    res.add(root.right)

            dfs(root.left)
            dfs(root.right)

            if root.left and root.left.val in delete:
                root.left = None
            if root.right and root.right.val in delete:
                root.right = None

        dfs(root)
        ans = []
        for x in res:
            if x.val not in delete:
                ans.append(x)

        return ans

            