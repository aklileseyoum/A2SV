class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        answer = right

        while left <= right:
            mid = (left + right) // 2

            ans = 0
            for num in nums:
                ans += math.ceil(num / mid)

            if ans <= threshold:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return answer