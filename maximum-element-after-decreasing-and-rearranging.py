class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for idx in range(1, len(arr)):
            arr[idx] = min((arr[idx - 1] + 1), arr[idx])

        return arr[-1]