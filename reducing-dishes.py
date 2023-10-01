class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        res = 0
        presum = 0
        for i in range(len(satisfaction)):
            presum += satisfaction[i]
            if presum < 0:
                break
            res += presum

        return res