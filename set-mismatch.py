class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        bucket = [[] for _ in range(len(nums))]
        for num in nums:
            bucket[num - 1].append(num)
        
        answer = [0] * 2
        for idx in range(len(bucket)):
            if len(bucket[idx]) > 1:
                answer[0] = bucket[idx][0]
            if len(bucket[idx]) == 0:
                answer[1] = idx + 1
            
        return answer