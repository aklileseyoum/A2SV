# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def traverse(root):
            if root == None:
                return

            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                traverse(root.left)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                traverse(root.right)

        traverse(root)
        answer = []
        visited = set()
        def bfs(node, step):
            if step == k:
                answer.append(node)
                return

            visited.add(node)
            for each in graph[node]:
                if each not in visited:
                    bfs(each, step+1)

        bfs(target.val, 0)
        return answer