class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)
        maxi = max(list(freq.values()))
        ans = float('inf')
        for k, v in freq.items():
            if v == maxi:
                idx1 = nums.index(k)
                idx2 = len(nums) - nums[::-1].index(k)
                ans = min(ans, (idx2 - idx1))

        return ans
        