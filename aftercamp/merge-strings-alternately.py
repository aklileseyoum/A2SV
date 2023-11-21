class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ans = ""
        for idx in range(min(len(word1), len(word2))):
            ans += word1[idx] + word2[idx]

        idx += 1
        if idx < len(word1):
            ans += word1[idx:]
        if idx < len(word2):
            ans += word2[idx:]

        return ans
            
