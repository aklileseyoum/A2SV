# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        store = defaultdict(list)
        priority_queue = [(0, 1, root)]
        
        while priority_queue:
            level, value, node = heapq.heappop(priority_queue)
            if len(store[level]) >= 2:
                store[level][-1] = value
            else:
                store[level].append(value)

            if node.left:
                heapq.heappush(priority_queue, (level + 1, 2 * value, node.left))
            if node.right:
                heapq.heappush(priority_queue, (level + 1, (2 * value + 1), node.right))


        nodes = list(store.values())
        maximum = 0
        
        for node in nodes:
            if len(node) > 1:
                diff = node[-1] - node[0]
                maximum = max(maximum, diff)

        return maximum + 1