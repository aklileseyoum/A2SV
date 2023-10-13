class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        no_swap = [len(nums1)] * len(nums1)
        swap = [len(nums2)] * len(nums2)
        no_swap[0] = 0
        swap[0] = 1
        for idx in range(1, len(nums1)):
            if nums1[idx - 1] < nums1[idx] and nums2[idx - 1] < nums2[idx]:
                no_swap[idx] = no_swap[idx - 1]
                swap[idx] = swap[idx - 1] + 1
            if nums1[idx - 1] < nums2[idx] and nums2[idx - 1] < nums1[idx]:
                no_swap[idx] = min(no_swap[idx], swap[idx - 1]) 
                swap[idx] = min(swap[idx], no_swap[idx - 1] + 1) 

        return min(no_swap[-1], swap[-1])