class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums = []
        heapify(nums)
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if len(nums) < k:
                    heappush(nums, -matrix[row][col])
                else:
                    val = -1 * heappop(nums)
                    if val > matrix[row][col]:
                        heappush(nums, -matrix[row][col])
                    else:
                        heappush(nums, -val)

        answer = -1 * heappop(nums)
        return answer