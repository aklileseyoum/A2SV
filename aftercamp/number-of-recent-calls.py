class RecentCounter:

    def __init__(self):
        self.time = []

    def ping(self, t: int) -> int:
        self.time.append(t)
        if t < 3000:
            return len(self.time)
        else:
            idx = bisect_left(self.time, t - 3000)
            return len(self.time) - idx


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)