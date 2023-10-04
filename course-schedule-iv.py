class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        courses = [[float('inf')] * numCourses for _ in range(numCourses)]
        for u, v in prerequisites:
            courses[u][v] = 1

        for i in range(numCourses):
            courses[i][i] = 0

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    courses[i][j] = min(courses[i][j], courses[i][k] + courses[k][j])

        answer = []
        for u, v in queries:
            if courses[u][v] == float(inf):
                answer.append(False)
            else:
                answer.append(True)

        return answer