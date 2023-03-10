# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        answer = []
        def backtracking(root, path):
            if root == None:
                return 

            path.append(str(root.val))
            if root.left == None and root.right == None:
                answer.append('->'.join(path))
                path.pop()
                return

            backtracking(root.left, path)
            backtracking(root.right, path)
            path.pop()
            

        backtracking(root, [])
        return answer