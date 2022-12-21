class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        i = 0
        j = 0
        a = ""
        while i < len(strs[0]) and j < len(strs[1]):
            if strs[0][i] == strs[1][i]:
                a += strs[0][i]
            else:
                break
            i += 1
            j += 1
        if len(strs) > 2:
            for i in range(2, len(strs)):
                x = len(a)
                y = strs[i]
                if a == y[:x]:
                    continue
                else:
                    a = a[:-1]
                    x -= 1
                    while a != y[:x] and x != 0:
                        a = a[:-1]
                        x -= 1
                    if x == 0:
                        return ""
        
        return a
