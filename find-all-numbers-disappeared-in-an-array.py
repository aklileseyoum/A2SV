class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        bucket = [0] * len(nums)
        for num in nums:
            bucket[num - 1] = num
        
        answer = []
        for idx in range(len(bucket)):
            if bucket[idx] == 0:
                answer.append(idx + 1)

        return answer