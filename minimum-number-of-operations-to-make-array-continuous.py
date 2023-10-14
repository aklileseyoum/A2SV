class Solution:
    def minOperations(self, nums: List[int]) -> int:

        def finder(shorter, num):
            left = 0
            right = len(shorter) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if shorter[mid] > num:
                    right = mid - 1
                elif shorter[mid] <= num:
                    left = mid + 1
               
            if num >= shorter[mid]:
                mid += 1
            return mid

        shorter = list(set(nums))
        shorter.sort()
        rangee = len(nums) - 1
        length_diff = len(nums) - len(shorter)
        ans = float("inf")
        for idx in range(len(shorter)):
            bound = shorter[idx] + rangee
            index = finder(shorter, bound)
            count = 0
            if index <= len(shorter):
                count += len(shorter) - index
            count += idx
            count += length_diff
            ans = min(ans, count)
        
        return ans