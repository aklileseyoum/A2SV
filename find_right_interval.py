class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = []
        for idx in range(len(intervals)):
            starts.append([intervals[idx][0], idx])
        starts.sort()

        answer = []
        for interval in intervals:
            left = 0
            right = len(starts) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2
                if starts[mid][0] == interval[1]:
                    ans = starts[mid][1]
                    break
                elif starts[mid][0] > interval[1]:
                    ans = starts[mid][1]
                    right = mid - 1
                else:
                    left = mid + 1

            answer.append(ans)

        return answer