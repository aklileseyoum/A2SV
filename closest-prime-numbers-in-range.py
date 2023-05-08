class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        isPrime = [True for _ in range(right + 1)]
        isPrime[0], isPrime[1] = False, False

        for num in range(right+1):
            if isPrime[num]:
                for each in range(num*num, right+1, num):
                    isPrime[each] = False

        primes = []
        for num in range(left, right+1):
            if isPrime[num]:
                primes.append(num)

        if len(primes) < 2:
            return [-1, -1]

        difference = []
        for idx in range(1, len(primes)):
            difference.append(primes[idx] - primes[idx - 1])


        index = difference.index(min(difference))
        return [primes[index], primes[index+1]]