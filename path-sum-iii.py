# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        answer = [0]
        def dfs(root, cursum, visited, count):
            if not root:
                return 
            
            count += 1
            if root.val == targetSum and count == 0:
                answer[-1] += 1
            else:
                cursum += root.val
                if cursum == targetSum:
                    answer[-1] += 1
                summ = cursum
                for each in visited:
                    summ -= each
                    if summ == targetSum:
                        answer[-1] += 1

            visited.append(root.val)
            dfs(root.left, cursum, visited, count)
            dfs(root.right, cursum, visited, count)
            visited.pop()


        dfs(root, 0, [], 0)
        return answer[-1]