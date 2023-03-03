class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        seen = defaultdict(int)
        prev = 0 
        answer = 0

        for idx in range(len(nums)):
            nums[idx] += prev
            prev = nums[idx]

        for num in nums:
            if num == goal:
                answer += 1
            if (num - goal) in seen:
                answer += seen[num - goal]

            seen[num] += 1

        return answer