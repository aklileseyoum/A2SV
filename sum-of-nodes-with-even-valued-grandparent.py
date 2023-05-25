# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.answer = 0

    def GrandChildren(self, root):
        grandchildren = 0
        if root.left:
            if root.left.left:
                grandchildren += root.left.left.val
            if root.left.right:
                grandchildren += root.left.right.val
        if root.right:
            if root.right.left:
                grandchildren += root.right.left.val
            if root.right.right:
                grandchildren += root.right.right.val

        return grandchildren


    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if root == None:
            return
        

        if root.val % 2 == 0:
            self.answer += self.GrandChildren(root)
            

        self.sumEvenGrandparent(root.left)
        self.sumEvenGrandparent(root.right)
            

        return self.answer