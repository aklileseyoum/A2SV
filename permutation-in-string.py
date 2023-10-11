class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        small = 0
        big = 0
        modulo = (10 ** 9) + 7
        for idx in range(len(s1)):
            small += (26 ** (ord(s1[idx]) - ord('a') + 1)) % modulo
            big += (26 ** (ord(s2[idx]) - ord('a') + 1)) % modulo

        if small == big:
            return True

        for idx in range(len(s1), len(s2)):
            big -= (26 ** (ord(s2[idx-len(s1)]) - ord('a') + 1)) % modulo
            big += (26 ** (ord(s2[idx]) - ord('a') + 1)) % modulo
            if small == big:
                return True