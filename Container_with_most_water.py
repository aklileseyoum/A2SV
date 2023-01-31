class Solution:
    def maxArea(self, height: List[int]) -> int:
        first = 0
        last = len(height) - 1
        maximum = 0

        while first < last:
            diff = last - first
            if height[first] < height[last]:
                prod = height[first] * diff
                first += 1
            else:
                prod = height[last] * diff
                last -= 1
            if prod > maximum:
                maximum = prod

        return maximum
