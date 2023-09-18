class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        divider = 2
        while n > 1:
            if n % divider:
                divider += 1
                continue
            n /= divider
            ans += divider

        return ans