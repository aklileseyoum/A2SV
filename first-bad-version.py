# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        right = n 
        left = 1

        while left <= right:
            mid = (right + left) // 2
            if right == left and isBadVersion(mid):
                return mid
            elif right == left + 1:
                if isBadVersion(left):
                    return left
                elif isBadVersion(right):
                    return right
            if not isBadVersion(mid):
                left = mid
            else:
                right = mid

        return n