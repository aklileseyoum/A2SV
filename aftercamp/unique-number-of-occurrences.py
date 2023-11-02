class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq = Counter(arr)
        values = list(freq.values())
        if len(set(values)) == len(values):
            return True

        