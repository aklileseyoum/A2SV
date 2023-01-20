class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        answer = []
        for num in nums:
            new = 0
            while num != 0:
                modulo = num % 10
                new = new * 10 + modulo
                num = num // 10
            answer.append(new)

        nums = nums + answer
        sett = set(nums)
        count = len(sett)
        
        return count
