class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        answer = []
        i = 0
        while i < len(nums):
            if nums[i]%2 == 0:
                answer.append(nums[i])
                nums.remove(nums[i])
            else:
                i += 1
        if len(nums) > 0:
            answer = answer + nums
                
        return answer
