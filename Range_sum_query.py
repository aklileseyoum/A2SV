class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        prev = 0
        for num in nums:
            self.prefix_sum.append(num+prev)
            prev += num

    def sumRange(self, left: int, right: int) -> int:
        
        if left != 0:
            answer = self.prefix_sum[right] - self.prefix_sum[left - 1]
        else:
            answer = self.prefix_sum[right]
        return answer
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
