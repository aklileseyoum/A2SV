# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        store = {}
        
        def see(root, level=0):
            if root == None:
                return

            if level not in store:
                store[level] = root.val

            see(root.right, level + 1)
            see(root.left, level + 1)
            
        see(root)
        return list(store.values())