class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        operations = 0
        first = 0
        last = len(nums) - 1
        nums.sort()
        while first < last:
            summ = nums[first] + nums[last]
            if summ > k:
                last -= 1
            elif summ < k:
                first += 1
            else:
                operations += 1
                first += 1
                last -= 1

        return operations
