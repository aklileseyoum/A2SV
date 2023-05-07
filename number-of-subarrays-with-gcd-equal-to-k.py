class Solution:
    def GCD(self, a, b):
        if b == 0:
            return a
        return self.GCD(b, a % b)

    def subarrayGCD(self, nums: List[int], k: int) -> int:
        answer = 0
        
        for idx in range(len(nums)):
            num = nums[idx]
            for idx2 in range(idx, len(nums)):
                num = self.GCD(num, nums[idx2])
                if num == k:
                    answer += 1

        return answer