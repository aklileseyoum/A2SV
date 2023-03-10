# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        store = defaultdict(list)
        
        def width(root, level=0, value=1):
            if root == None:
                return

            if len(store[level]) > 2:
                store[level][-1] = value
            else:
                store[level].append(value)
            
            width(root.left, level + 1, 2 * value)
            width(root.right, level + 1, 2 * value + 1)
        
        width(root)
        nodes = list(store.values())
        maximum = 0
        
        for node in nodes:
            if len(node) > 1:
                diff = node[-1] - node[0]
                maximum = max(maximum, diff)

        return maximum + 1