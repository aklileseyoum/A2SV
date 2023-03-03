class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return x
        left = 0
        right = x // 2
        mid = (right + left) // 2
        while left <= right:
            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid + 1
            else:
                return mid
            mid = (right + left) // 2

        return mid