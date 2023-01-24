class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        last = len(numbers)-1
        while first != last:
            summ = numbers[first] + numbers[last]
            if summ == target:
                return ([first+1,last+1])
            elif summ > target:
                last -= 1
            else:
                first += 1
