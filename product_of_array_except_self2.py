class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        for num in nums:
            prod *= num

        if prod == 0:
            count = nums.count(0)
            zeros_prod = 1
            for num in nums:
                if num != 0:
                    zeros_prod *= num

        answer = []
        if prod == 0:
            if count > 1:
                answer = [0 for num in nums]
            else: 
                for num in nums:
                    if num == 0:
                        answer.append(zeros_prod)
                    else:
                        answer.append(0)
        else:
            for num in nums:
                answer.append(int(prod / num))

        return answer
