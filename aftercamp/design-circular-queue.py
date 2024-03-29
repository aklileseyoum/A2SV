class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue = [-1 for _ in range(k)]
        self.start = 0
        self.end = 0

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.queue[self.end] = value
            self.end += 1
            if self.end == len(self.queue):
                self.end = 0
            return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if not self.isEmpty():
            self.queue[self.start] = -1
            self.start += 1
            if self.start == len(self.queue):
                self.start = 0
            return True

    def Front(self):
        """
        :rtype: int
        """
        if not self.isEmpty():
            return self.queue[self.start]
        return -1  

    def Rear(self):
        """
        :rtype: int
        """
        if not self.isEmpty():
            return self.queue[self.end -1]
        return -1

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.start == self.end and self.queue[self.start] == -1:
            return True

    def isFull(self):
        """
        :rtype: bool
        """
        if self.start == self.end and self.queue[self.start] != -1:
            return True
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()