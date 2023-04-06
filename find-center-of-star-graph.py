class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        common = set(edges[0]).intersection(edges[1])
        for each in common:
            return each