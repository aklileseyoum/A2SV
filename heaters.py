class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def closest(heaters, house):
            l, r = 0, len(heaters) - 1
            while l <= r:
                mid = l + (r-l) // 2
                if heaters[mid] < house:
                    l = mid + 1
                elif heaters[mid] > house:
                    r = mid - 1
                else:
                    l = mid
                    break
            leftCount = rightCount= float("inf")
            if l < len(heaters):
                leftCount = abs(heaters[l] -house )
            if r > -1:
                rightCount = abs(heaters[r]- house)               
            return min(leftCount, rightCount)

        heaters.sort()
        radius = 0
        for house in houses:
            radius = max(radius, closest(heaters, house))
        return radius