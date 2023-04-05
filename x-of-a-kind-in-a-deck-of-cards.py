class Solution:
    def GCD(self, a, b):
        if b == 0:
            return a
        return self.GCD(b, a%b)

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        freq = set(count.values())
        if len(freq) == 1 and 1 not in freq:
            return True
        
        freq = list(freq)
        gcd = freq[0]
        for idx in range(1, len(freq)):
            maximum = max(gcd, freq[idx])
            minimum = min(gcd, freq[idx])
            gcd = self.GCD(maximum, minimum)

        if gcd != 1:
            return True