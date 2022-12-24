class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 2
        j = 0
        result = ""
        while j < len(s):
            if i < len(s) and s[i] == '#':
                x = int(s[i-2:i])
                x += 96
                result += chr(x)
                i += 3
                j +=3
            else:
                x = int(s[j]) + 96
                result += chr(x)
                j += 1
                i += 1

        return result
