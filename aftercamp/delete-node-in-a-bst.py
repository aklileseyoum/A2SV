# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def dfs(root, parent, leftie):
            if not root:
                return True
            
            if root.val == key:
                val = searchMini(root)
                if val == float('inf'):
                    yes = [0]
                    boolean = deleteVal(parent, root, key, leftie)
                    if not boolean:
                        return False
                else:
                    root.val = val
                    deleteVal(root, root.left, val, True)
                    deleteVal(root, root.right, val, False)

            val1 = True
            val2 = True
            if root and key > root.val:
                val1 = dfs(root.right, root, False)
            if root and key < root.val:
                val2 = dfs(root.left, root, True)

            return val1 and val2

        def searchMini(root):
            if root.right:
                root = root.right
                val = root.val
                while root.left:
                    val = root.left.val
                    root = root.left
            elif root.left:
                root = root.left
                val = root.val
                while root.right:
                    val = root.right.val
                    root = root.right
            else:
                val = float('inf')
            return val

        def deleteVal(parent, root, val, leftie):
            if not root:
                return True

            if root.val == val:
                if not root.left and not root.right:
                    if not parent:
                        return False
                    else:
                        if leftie:
                            parent.left = None
                        else:
                            parent.right = None
                else:
                    new = searchMini(root)
                    if new == float('inf'):
                        if leftie:
                            parent.left = None
                        else:
                            parent.right = None
                    else:
                        root.val = new
                        return deleteVal(root, root.right, new, False) and deleteVal(root, root.left, new, True)     

            return deleteVal(root, root.left, val, True) and deleteVal(root, root.right, val, False)
            

        if not dfs(root, None, True):
            return None

        return root
        