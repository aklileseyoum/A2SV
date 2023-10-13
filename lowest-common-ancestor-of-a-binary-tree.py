# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        priority_queue = [(root.val, root)]
        parent = defaultdict(list)
        parent[root.val] = [None]
        count = 0
        while priority_queue:
            value, node = heapq.heappop(priority_queue)
            if value == p or value == q:
                count += 1
            if count >= 2:
                break

            if node.left:
                parent[node.left].append(node)
                heapq.heappush(priority_queue,(node.left.val, node.left))

            if node.right:
                parent[node.right].append(node)
                heapq.heappush(priority_queue,(node.right.val, node.right))

        def dfs(node, beSet):
            if beSet:
                ans = set()
            else:
                ans = []
            while node:
                if beSet:
                    ans.add(node)
                else:
                    ans.append(node)
                
                if len(parent[node]) > 0:
                    node = parent[node][-1]
                else:
                    node = None
            return ans
        
        p_anc = dfs(p, True)
        q_anc = dfs(q, False)
        
        for each in q_anc:
            if each in p_anc:
                return each

        return root