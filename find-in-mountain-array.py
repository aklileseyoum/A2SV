# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        left = 0
        right = length - 1
        memo = {}
        
        while left <= right:
            mid = left + (right - left) // 2
            if mid not in memo:
                memo[mid] = mountain_arr.get(mid)
            val = memo[mid]
            toLeft = -1
            toRight = -1
            if mid - 1 >= 0:
                if mid - 1 not in memo:
                    memo[mid - 1] = mountain_arr.get(mid - 1)
                toLeft = memo[mid - 1]
            if mid + 1 < length:
                if mid + 1 not in memo:
                    memo[mid + 1] = mountain_arr.get(mid + 1)
                toRight = memo[mid + 1]
            if toLeft > val > toRight:
                right = mid - 1
            elif toLeft < val < toRight:
                left = mid + 1
            elif toLeft < val > toRight:
                peak_idx = mid
                peak_val = val
                break
                
        if peak_val == target:
            return peak_idx

        left = 0
        right = peak_idx
        while left <= right:
            mid = left + (right - left) // 2
            if mid not in memo:
                memo[mid] = mountain_arr.get(mid)
            val = memo[mid]
            if val < target:
                left = mid + 1
            elif val > target:
                right = mid - 1
            else:
                return mid

        left = peak_idx
        right = length - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid not in memo:
                memo[mid] = mountain_arr.get(mid)
            val = memo[mid]
            if val > target:
                left = mid + 1
            elif val < target:
                right = mid - 1
            else:
                return mid

        return -1