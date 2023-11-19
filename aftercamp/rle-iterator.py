class RLEIterator(object):

    def __init__(self, encoding):
        """
        :type encoding: List[int]
        """
        self.idx = 0
        self.freq = [0]
        self.values =[]
        for idx in range(1, len(encoding), 2):
            if encoding[idx - 1] > 0:
                self.values.append(encoding[idx])
                self.freq.append(self.freq[-1] + encoding[idx - 1])

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.idx += n
        for index in range(len(self.freq)):
            if self.idx <= self.freq[index]:
                break
        
        if index - 1 >= len(self.values) or self.idx > self.freq[-1]:
            return -1

        return self.values[index - 1]



# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)