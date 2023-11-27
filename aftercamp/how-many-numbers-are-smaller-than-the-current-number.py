class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        ans = []
        for each in nums:
            ans.append(sorted_nums.index(each))

        return ans