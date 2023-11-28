class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [nums[0]]
        for idx in range(1, len(nums)):
            ans.append(ans[-1] + nums[idx])

        return ans