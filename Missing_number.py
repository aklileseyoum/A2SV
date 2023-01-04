class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maximum = max(nums)
        summ = 0
        for i in range(maximum + 1):
            summ += i   

        summ2 = 0
        for i in nums:
            summ2 += i

        diff = summ - summ2
        if diff > 0:
            return diff
        else:
            if 0 not in nums:
                return 0
            else:
                return (maximum + 1)  
