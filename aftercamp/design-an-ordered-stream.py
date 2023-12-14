class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.container =["" for _ in range(n)]
        self.count = 1
        

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.container[idKey - 1] = value
        ans = []
        if self.count == idKey:
            idx = idKey - 1
            while idx < len(self.container) and self.container[idx] != "":
                ans.append(self.container[idx])
                idx += 1
            
            self.count = idx + 1

        return ans
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)