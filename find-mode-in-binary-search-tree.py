# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Traversal(self, root):
        if root == None:
            return []

        array = [root.val]
        array += self.Traversal(root.left)
        array += self.Traversal(root.right)

        return array
        
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = Counter(self.Traversal(root))
        maximum = max(freq.values())
        
        answer = []
        for key, value in freq.items():
            if value == maximum:
                answer.append(key)

        return answer