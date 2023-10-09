# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
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
            distances = {}
            visited = set()
            priority_queue = []
            if root:
                priority_queue = [[root.val, root.val, graph[root][-1]]]
                parent[graph[root][-1]] = [-1]
            
            while priority_queue:
                current_distance, node_val, current_node_rep = heapq.heappop(priority_queue)
                if current_node_rep in visited:
                    continue
                visited.add(current_node_rep)

                current_node = graph[current_node_rep][-1]
                if not current_node.left and not current_node.right:
                    distances[current_node] = current_distance

                if current_node.left:
                    distance = current_distance + current_node.left.val
                    parent[graph[current_node.left][-1]].append(graph[current_node][-1])
                    heapq.heappush(priority_queue, [distance, current_node.left.val, graph[current_node.left][-1]])

                if current_node.right:
                    distance = current_distance  + current_node.right.val
                    parent[graph[current_node.right][-1]].append(graph[current_node][-1])
                    heapq.heappush(priority_queue, [distance, current_node.right.val, graph[current_node.right][-1]])
                
            return distances

        parent = defaultdict(list)
        ans = dijkstra()
        
        answer = []
        for k, v in ans.items():
            if v == targetSum:
                each = [k.val]
                node = graph[k][-1]
                while parent[node][-1] != -1:
                    node = parent[node][-1]
                    each.append(graph[node][-1].val)
                answer.append(each[::-1])

        return answer