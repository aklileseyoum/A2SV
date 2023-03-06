class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = 0
        

        for weight in weights:
            right += weight

        answer = right

        while left <= right:
            mid = (left + right) // 2
            
            day = 0
            total = 0

            for weight in weights:
                total += weight
                if total == mid:
                    day += 1
                    total = 0
                elif total > mid:
                    day += 1
                    total = weight

            if total >= weight:
                day += 1

            if day <= days:
                answer = min(answer, mid)
                right = mid - 1
            else:
                left = mid + 1

        return answer