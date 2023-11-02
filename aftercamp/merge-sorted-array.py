class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while len(nums1) > m:
            nums1.pop()

        for each in nums2:
            index = bisect.bisect_left(nums1, each)
            nums1.insert(index, each)
            