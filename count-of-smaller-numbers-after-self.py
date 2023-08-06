class Solution:
    def mergeSort(self, left, right, arr):
        if left == right:
            return [(arr[left],left)]
        mid = left + (right - left) // 2
        left_half = self.mergeSort(left, mid, arr)
        right_half = self.mergeSort(mid + 1, right, arr)

        return self.merge(left_half, right_half)

    def merge(self, left_half, right_half):
        pt1 = len(left_half) - 1
        pt2 = len(right_half) - 1
        while pt1 >= 0 and pt2 >= 0:
            if left_half[pt1][0] > right_half[pt2][0]:
                self.answer[left_half[pt1][1]] += pt2 + 1
                pt1 -= 1
            else:
                pt2 -= 1

        idx1 = 0
        idx2 = 0
        merged = []
        while idx1 < len(left_half) and idx2 < len(right_half):
            if left_half[idx1] < right_half[idx2]:
                merged.append(left_half[idx1])
                idx1 += 1
            else:
                merged.append(right_half[idx2])
                idx2 += 1

        if idx1 < len(left_half):
            merged += left_half[idx1:]

        if idx2 < len(right_half):
            merged += right_half[idx2:]

        return merged

    def countSmaller(self, nums: List[int]) -> List[int]:
        self.answer = [0 for _ in range(len(nums))]
        self.mergeSort(0, len(nums)-1, nums)
        return self.answer