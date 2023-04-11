"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        answer = [0]
        def dfs(id1):
            for employe in employees:
                if employe.id == id1:
                    save = employe
                    break

            answer[-1] += save.importance
            for subordinate in save.subordinates:
                dfs(subordinate)

        dfs(id)
        return answer[-1]