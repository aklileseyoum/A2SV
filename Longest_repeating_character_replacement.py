class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        window = defaultdict(int)
        total = 0
        max_len = 0
        
        for right in range(len(s)):
            total += 1
            window[s[right]] += 1
            maximum = max(window.values())
            while total - maximum > k:
                max_len = max(max_len, total - 1)
                total -= 1
                window[s[left]] -= 1
                maximum = max(window.values())
                left += 1

        max_len = max(max_len, total)

        return max_len
