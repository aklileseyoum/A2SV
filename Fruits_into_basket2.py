class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        from collections import defaultdict

        picked = defaultdict(int)
        left = 0
        right = 0
        max_len = 0

        for right in range(len(fruits)):
            picked[fruits[right]] += 1
            while len(picked) >= 3:
                if fruits[left] in picked:
                    picked[fruits[left]] -= 1
                    if picked[fruits[left]] == 0:
                        del picked[fruits[left]]
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len
