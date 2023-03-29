class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        frequency = [[] for _ in range(max(freq.values()) + 1)]

        for key, value in freq.items():
            frequency[value].append(key)
        
        answer = []
        while k > 0:
            listt = frequency.pop()
            answer += listt
            k -= len(listt)

        return answer
        