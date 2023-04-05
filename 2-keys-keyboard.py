class Solution:
    def isPrime(self, num):
        d = 2
        while d * d <= num:
            if num % d == 0:
                return False
            d += 1
        return True
        
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        if self.isPrime(n):
            return n
        
        answer = 0
        divisor = 2
        while n > 1:
            if n % divisor != 0:
                divisor += 1
            else:
                answer += divisor
                n = n // divisor

        return answer