class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        summ = 0
        while i < k:
            summ += nums[i]
            i += 1
        max_average = summ / k
        idx1 = 0
        idx2 = k
        while idx2 < len(nums):
            summ += nums[idx2] - nums[idx1]
            if max_average < (summ/k):
                max_average = summ / k
            idx1 += 1
            idx2 += 1

        return max_average
