class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = Counter(s)
        visited = set()
        ans = 0
        for idx in range(len(s)):
            if s[idx] not in visited and freq[s[idx]] > 1:
                index = len(s) - (s[::-1].index(s[idx])) - 1
                ans += len(set(s[idx+1:index]))
                visited.add(s[idx])

        return ans
        