class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import defaultdict
        target = defaultdict(int)
        for character in p:
            target[character] += 1

        window = defaultdict(int)
        for character in s[:len(p)]:
            window[character] += 1

        idx1 = 0
        idx2 = len(p) 
        answer = []
        while idx2 < len(s):
            print(window)
            if target == window:
                answer.append(idx1)
            if s[idx1] in window:
                window[s[idx1]] -= 1
                if window[s[idx1]] == 0:
                    window.pop(s[idx1])
            window[s[idx2]] += 1
            idx1 += 1
            idx2 += 1
        
        if target == window:
            answer.append(idx1)

        return answer
