class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        def getPower(num):
            ans = 0
            while num > 1:
                if num % 2 == 0:
                    num //= 2
                else:
                    num *= 3
                    num += 1
                ans += 1
            return ans

        power = []
        for no in range(lo, hi+1):
            power.append([getPower(no), no])

        power.sort()
        
        return power[k-1][1]
