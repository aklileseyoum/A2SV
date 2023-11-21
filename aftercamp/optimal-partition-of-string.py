class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        visited = set()
        ans = 0
        for idx in range(len(s)):
            if s[idx] in visited:
                ans += 1
                visited = set()
            visited.add(s[idx])

        return ans+1
        