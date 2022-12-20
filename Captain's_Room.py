# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
nums = list(map(int, input().split(" ")))
nums.sort()
i = 0
while i < len(nums):
    if i+1 < len(nums) and nums[i] == nums[i+1]:
        i += k
    else:
        print(nums[i])
        break
