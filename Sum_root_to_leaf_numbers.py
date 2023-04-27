# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        answer = []
        def dfs(root, num, parent):
            if not root:
                if not parent.left and not parent.right:
                    answer.append(int(num))
                    num = ""
                return

            num += str(root.val)

            dfs(root.left, num, root)
            dfs(root.right, num, root)

        dfs(root, "", root)
        return (sum(answer)//2)