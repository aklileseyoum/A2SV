class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        
        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                added = nums1[i] + nums2[j]
                if len(heap) < k:
                    heappush(heap, (-added, nums1[i], nums2[j]))
                else:
                    if added > -heap[0][0]:
                        break
                    else:
                        heappushpop(heap, (-added, nums1[i], nums2[j]))

        return [[first, second] for (_, first, second) in heap]