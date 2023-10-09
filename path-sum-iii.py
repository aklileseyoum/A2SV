# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        graph = defaultdict(list)
        def dfs(root):
            if not root:
                return

            graph[root].append(parent[-1])
            graph[parent[-1]].append(root)
            parent[-1] += 1
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)

        parent = [1]
        dfs(root)
        
        def dijkstra():
            visited = set()
            added = defaultdict(list)
            priority_queue = []
            ans = 0
            if root:
                priority_queue = [[root.val, root.val, graph[root][-1]]]
                added[graph[root][-1]] = [root.val]
            
            while priority_queue:
                current_distance, node_val, current_node_rep = heapq.heappop(priority_queue)
                if current_node_rep in visited:
                    continue
                visited.add(current_node_rep)

                current_node = graph[current_node_rep][-1]
                summed = list(added[graph[current_node][-1]])[::-1]
                val = current_distance
                
                while summed:
                    if val == targetSum:
                        ans += 1
                    val -= summed.pop()

                if current_node.left:
                    distance = current_distance + current_node.left.val
                    added[graph[current_node.left][-1]] += added[graph[current_node][-1]]
                    added[graph[current_node.left][-1]].append(current_node.left.val)
                    heapq.heappush(priority_queue, [distance, current_node.left.val, graph[current_node.left][-1]])

                if current_node.right:
                    distance = current_distance  + current_node.right.val
                    added[graph[current_node.right][-1]] += added[graph[current_node][-1]]
                    added[graph[current_node.right][-1]].append(current_node.right.val)
                    heapq.heappush(priority_queue, [distance, current_node.right.val, graph[current_node.right][-1]])
                
            return ans

        return dijkstra()