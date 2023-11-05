class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ans = 0
        saved = set()
        for idx in range(len(words)-1, -1, -1):
            if words[idx][::-1] in saved:
                ans += 1
            else:
                saved.add(words[idx])

        return ans