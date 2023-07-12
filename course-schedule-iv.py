class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)

        def dfs(course):
            if course not in pre:
                pre[course] = set()
                for each in graph[course]:
                    pre[course].add(each)
                    pre[course] |= dfs(each)

            return pre[course]

        pre = {}
        for course in range(numCourses):
            dfs(course)
        
        answer = []
        for u, v in queries:
            answer.append(u in pre[v])
        
        return answer