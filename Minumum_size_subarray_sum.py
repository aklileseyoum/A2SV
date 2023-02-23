class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        summ = nums[left]
        min_len = len(nums) + 1

        for right in range(1, len(nums)):
            while target <= summ:
                size = right - left
                if min_len > size:
                    min_len = size
                print(min_len)
                summ -= nums[left]
                left += 1

            summ += nums[right]
        
        while target <= summ:
                size = right - left + 1
                if min_len > size:
                    min_len = size
                summ -= nums[left]
                left += 1

        if min_len > len(nums):
            min_len = 0

        return min_len
