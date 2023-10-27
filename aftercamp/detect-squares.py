class DetectSquares(object):

    def __init__(self):
        self.x_axis = defaultdict(set)
        self.y_axis = defaultdict(set)
        self.freq = defaultdict(int)

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        x, y = point
        self.x_axis[x].add((x, y))
        self.y_axis[y].add((x, y))
        self.freq[(x, y)] += 1

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        def dfs(x, y, level, diff, val, not_x):
            if level == 3:
                if (point[0] == x and point[1] != y) or (point[0] != x and point[1] == y):
                    new[-1] += val
                return 
                
            if not_x:
                for new_x, new_y in self.y_axis[y]:
                    if abs(new_x - x) == diff:
                        value = self.freq[(new_x, new_y)]
                        dfs(new_x, new_y, level+1, diff, value*val, (not not_x))         
            else:
                for new_x, new_y in self.x_axis[x]:
                    if abs(new_y - y) == diff:
                        value = self.freq[(new_x, new_y)]
                        dfs(new_x, new_y, level+1, diff, value*val, (not not_x))

        x, y = point
        ans = 0
        for new_x, new_y in self.x_axis[x]:
            new = [0]
            diff = abs(y - new_y)
            dfs(new_x, new_y, 1, diff, self.freq[(new_x, new_y)], True)
            ans += new[-1]

        return ans
    


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)