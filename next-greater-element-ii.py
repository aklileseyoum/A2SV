class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        length = len(nums)
        counter = defaultdict(list)

        for idx in range(length * 2):
            while stack and stack[-1] < nums[idx % length]:
                counter[stack.pop()].append(nums[idx % length])
            stack.append(nums[idx % length])
       
        answer = []
        for num in nums:
            if len(counter[num]) > 0:
                answer.append(counter[num].pop(0))
            else:
                answer.append(-1)

        return answer