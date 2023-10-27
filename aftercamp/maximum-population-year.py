class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        maxi = 0
        save = defaultdict(int)
        for birth, death in logs:
            if save[birth] != 0:
                continue
            for b, d in logs:
                if birth >= b and birth < d:
                    save[birth] += 1
            maxi = max(save[birth], maxi)

        ans = float('inf')
        for k, v in save.items():
            if v == maxi:
                ans = min(ans, k)
        
        return ans