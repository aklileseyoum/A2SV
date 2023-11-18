class Solution(object):
    def maxStrength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zero = nums.count(0)
        new = []
        for num in nums:
            if num != 0:
                new.append(num)
        if len(new) == 0:
            return 0
            
        if len(new) == 1:
            if zero > 0:
                return max(0, new[-1])
            return new[-1]
        ans = 1
        neg = []
        for num in new:
            if num > 0:
                ans *= num
            elif num < 0:
                neg.append(num)

        neg.sort()
        if len(neg) % 2 != 0:
            neg.pop()
        
        for num in neg:
            ans *= num
        
        if zero > 0:
            return max(ans, 0)

        return ans
