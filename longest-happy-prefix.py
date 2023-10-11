class Solution:
    def longestPrefix(self, s: str) -> str:
        lps = [0] * len(s)
        prev, i = 0, 1
        while i < len(s):
            if s[prev] == s[i]:
                lps[i] = prev + 1
                prev += 1
                i += 1
            else:
                if prev == 0:
                    i += 1
                else:
                    prev = lps[prev - 1]

        maximum = max(lps)
        ans = ""
        idx = len(s) - 1
        ans = s[idx - lps[idx] + 1 : idx + 1]

        return ans