class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = bisect_left(nums, target)
        last = bisect_right(nums,target)
        answer = []

        if len(nums) == 1 and nums[0] == target:
            return [0, 0]
        print(first, last)
        if first < len(nums) and nums[first] == target:
            answer.append(first)
        else:
            answer.append(-1)

        if last != 0 and last < len(nums) + 1 and nums[last - 1] == target:
            answer.append(last - 1)
        else:
            answer.append(-1)

        return answer
