class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        largest=0

        nums.sort()
        rightp=len(nums)-1

        
        while rightp>1:
            num1=nums[rightp-1]
            num2=nums[rightp-2]
            if  num1+num2>nums[rightp]:

                
                largest=num1+num2+nums[rightp]
                break
            rightp-=1
        return largest
