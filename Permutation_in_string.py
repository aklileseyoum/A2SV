class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict

        if len(s1) > len(s2):
            return False
            
        checker = defaultdict(int)
        for s in s1:
            checker[s] += 1

        window = defaultdict(int)
        for idx in range(len(s1)):
            window[s2[idx]] += 1

        left = 0
        right = len(s1)

        while right < len(s2):
            if checker == window:
                return True
            if s2[left] in window:
                if window[s2[left]] > 1:
                    window[s2[left]] -= 1
                else:
                    del window[s2[left]]
            window[s2[right]] += 1
            left += 1
            right += 1

        print(window)
        if checker == window:
            return True

        return False
