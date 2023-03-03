class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                break
            elif arr[mid - 1] < arr[mid] < arr[mid + 1]:
                left = mid
            else:
                right = mid

        return mid