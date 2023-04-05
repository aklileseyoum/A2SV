class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        xor = 0
        for key in count.keys():
            xor ^= key
            
        xor2 = 0
        for key, value in count.items():
            if value == 3:
                xor2 ^= key
                
        return (xor^xor2)