class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        word = 0
        big = 0
        for idx in range(len(needle)):
            word += (26 ** (len(needle) - idx - 1)) * (ord(needle[idx]) - ord('a') + 1)
            big += (26 ** (len(needle) - idx - 1)) * (ord(haystack[idx]) - ord('a') + 1)
        
        if word == big:
            return 0

        for idx in range(len(needle), len(haystack)):
            big -= (26 ** (len(needle) - 1) * (ord(haystack[idx - len(needle)]) - ord('a') + 1))
            big *= 26
            big += (ord(haystack[idx]) - ord('a') + 1)
            if word == big:
                return (idx - len(needle) + 1)
        
        return -1