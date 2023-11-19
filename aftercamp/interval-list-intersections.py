class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        idx1 = 0
        idx2 = 0
        ans = []
        while idx1 < len(firstList) and idx2 < len(secondList):
            fStart, fEnd = firstList[idx1]
            sStart, sEnd = secondList[idx2]
            if max(fStart, sStart) <= min(fEnd, sEnd):
                ans.append([max(fStart, sStart), min(fEnd, sEnd)])

            if fEnd < sEnd:
                idx1 += 1
            else:
                idx2 += 1
            
        return ans
        