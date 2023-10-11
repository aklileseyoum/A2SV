class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        hashed = 0
        
        arr = [1]
        for i in range(1, k):
            arr.append(power * arr[-1])
        i = 0
        while i < k:
            hashed += (ord(s[i]) - ord('a') + 1) * (arr[i])
            i += 1
        
        if hashed % modulo == hashValue:
            return s[:k]
        
        ans = deque(s[:k])
        for idx in range(k, len(s)):
            hashed -= ord(s[idx - k]) - ord('a') + 1
            hashed //= power
            hashed += (ord(s[idx]) - ord('a') + 1) * (arr[k-1])
            ans.popleft()
            ans += s[idx]
            if hashed % modulo == hashValue:
                return ''.join(ans)