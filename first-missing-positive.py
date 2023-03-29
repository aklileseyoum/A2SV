class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        positives = set()
        for num in nums:
            if num > 0:
                positives.add(num)

        positives = list(positives)
        minimum = float('inf')
        checker = Counter(positives)
        
        for idx in range(len(positives)):
            number = positives[idx] - 1
            if number != 0 and checker[number] == 0:
                minimum = min(minimum, number)
        
        if minimum == float('inf'):
            return len(positives) + 1

        for num in range(1, minimum + 1):
            if checker[num] == 0:
                return int(num)