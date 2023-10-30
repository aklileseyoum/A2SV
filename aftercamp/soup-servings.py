class Solution(object):
    def soupServings(self, n):
        """
        :type n: int
        :rtype: float
        """
        if n >= 4300:
            return 1.0

        memo = {}
        def serve(a, b):
            if (a, b) not in memo:
                if a <= 0 and b <= 0:
                    return 0.5
                if a <= 0:
                    return 1.0
                if b <= 0:
                    return 0.0
                memo[(a, b)] = 0.25 * ((serve(a - 100, b)) + (serve(a - 75, b - 25)) + (serve(a - 50, b - 50)) + (serve(a - 25, b - 75)))

            return memo[(a, b)]

        return serve(n, n)