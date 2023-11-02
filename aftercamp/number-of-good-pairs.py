class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def comb(n):
            return (math.factorial(n) / (math.factorial(2) * math.factorial(n - 2)))
        
        freq = Counter(nums)
        ans = 0
        
        for val in freq.values():
            if val != 1:
                ans += comb(val)

        return ans