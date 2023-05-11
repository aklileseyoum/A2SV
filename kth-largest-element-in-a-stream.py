class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []
        while nums:
            heapify(nums)
            self.nums.append(heappop(nums))       
        
    def add(self, val: int) -> int:
        idx = bisect_left(self.nums, val)
        self.nums.insert(idx, val)
        
        return self.nums[-self.k]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)