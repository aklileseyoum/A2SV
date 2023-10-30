class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        set_arr = set(arr)
        count = 0
        num = 1
        while count != k:
            if num not in set_arr:
                count += 1
            if count == k:
                return num
            num += 1
        