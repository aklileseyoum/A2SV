class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mini = []
        for num in nums:
            if not mini:
                mini.append(num)
            else:
                if mini[-1] < num:
                    mini.append(mini[-1])
                else:
                    mini.append(num)

        stack = []
        for idx in range(len(nums)-1, -1, -1):
            if not stack:
                stack.append(nums[idx])
            else:
                while stack and stack[-1] < nums[idx]:
                    top = stack.pop()
                    if mini[idx] < top:
                        return True

                stack.append(nums[idx])
                
        