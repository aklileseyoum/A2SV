class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = [[1]]
        if numRows > 1:
            ans.append([1,1])
        while numRows > 2:
            new = [1]
            for idx in range(1, len(ans[-1])):
                new.append(ans[-1][idx] + ans[-1][idx - 1])

            new.append(1)
            ans.append(new)
            numRows -= 1
            
        return ans