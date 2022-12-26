class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minimum = float('inf')

        index = -1
        for point in points:
            if point[0] == x:
                distance = abs(y - point[1])
                if minimum > distance:
                    minimum = distance
                    index = points.index(point)
            elif point[1] == y:
                distance = abs(x - point[0])
                if minimum > distance:
                    minimum = distance
                    index = points.index(point)
        
        return index
