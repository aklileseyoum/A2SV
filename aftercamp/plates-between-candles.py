class Solution(object):
    def platesBetweenCandles(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        index = []
        for idx in range(len(s)):
            if s[idx] == '|':
                index.append(idx)

        ans = []
        for left, right in queries:
            idx1 = bisect_left(index, left)
            idx2 = bisect_left(index, right)
            if idx2 >= len(index) or idx2 < len(index) and index[idx2] > right:
                idx2 -= 1
            
            if idx1 >= idx2:
                ans.append(0)
            else:
                ans.append(index[idx2] - index[idx1] - (idx2 - idx1 - 1) - 1)

        return ans
        