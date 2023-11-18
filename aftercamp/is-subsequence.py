class Solution:
    def isSubsequence(self, s, t):
        idx1 = 0
        idx2 = 0
        while idx1 < len(t) and idx2 < len(s):
            if s[idx2] == t[idx1]:
                idx2 += 1
            idx1 += 1

        return idx2 == len(s)