class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        loses = {}
        for winner, loser in matches:
            if winner not in loses:
                loses[winner] = 0
            if loser not in loses:
                loses[loser] = 1
            else:
                loses[loser] += 1

        ans = [[] for _ in range(2)]
        for k, v in loses.items():
            if v == 0 or v == 1:
               ans[v].append(k)

        ans[0].sort()
        ans[1].sort()
        return ans
            
        