class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations)-1
        length = len(citations)

        while left <= right:
            mid = (left + right) // 2
            if (length - mid) < citations[mid]:
                right = mid - 1
            elif (length - mid) > citations[mid]:
                left = mid + 1
            else:
                return citations[mid]

        return length - left
        