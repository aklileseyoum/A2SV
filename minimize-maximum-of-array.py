class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        nums.reverse()
        left = 0
        right = 10 ** 9

        def good(target):
            carry = 0
            for x in nums:
                x += carry
                carry = 0
                if x >= target:
                    carry = x - target

            return carry == 0

        while left < right:
            mid = (left + right) // 2
            if good(mid):
                right = mid
            else:
                left = mid + 1

        return left