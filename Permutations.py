class Solution:
    def __init__(self):
        self.bit = 0
        self.neg_bit = 0
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        path = []
        check = set()
        def backtracking(index):
            if index >= len(nums):
                if len(path) == len(nums):
                    answer.append(path.copy())
                return
            for i in range(len(nums)+1):
                if i >= len(nums):
                    backtracking(i)
                elif nums[i] >= 0:
                    checker = 1 << nums[i]
                    if self.bit & (1 << nums[i]) < checker:
                        path.append(nums[i])
                        self.bit |= (1 << nums[i])
                        backtracking(i)
                        path.pop()
                        self.bit &= ~(1 << nums[i])
                elif nums[i] < 0:
                    checker = 1 << abs(nums[i])
                    if self.neg_bit & (1 << abs(nums[i])) < checker:
                        path.append(nums[i])
                        self.neg_bit |= (1 << abs(nums[i]))
                        backtracking(i)
                        path.pop()
                        self.neg_bit &= ~(1 << abs(nums[i]))
                
                    
                        
        backtracking(0)
        return answer