class Solution:
    def isPrime(self, num):
        d = 2
        while d * d <= num:
            if num % d == 0:
                return False
            d += 1
        return True

    def distinctPrimeFactors(self, nums: List[int]) -> int:
        answer = 0
        seen = set()
        for num in nums:
            divisor = 2
            while not self.isPrime(num):
                if num % divisor == 0:
                    num //= divisor
                    seen.add(divisor)
                else:
                    divisor += 1
            seen.add(num)

        return len(seen)