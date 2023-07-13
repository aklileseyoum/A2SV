class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num1 = float(inf)
        num2 = float(inf)
        for each in nums:
            if each > num2:
                return True
            if each > num1:
                num2 = min(each, num2)
            num1 = min(each, num1)

        return False