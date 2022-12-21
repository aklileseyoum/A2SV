class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        ans = 0
        k = x
        while x >= 1:
            y = x%10
            ans += y
            ans *= 10
            x = x//10
        ans = ans/10
        if k == ans:
            return True
        else:
            return False
