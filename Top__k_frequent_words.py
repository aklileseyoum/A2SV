class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        freq = defaultdict(int)
        for word in words:
            freq[word] += 1
        
        values = list(freq.values())
        value = [-i for i in values]
        answer = []
        count = k
        
        while count > 0:
            count -= 1
            heapify(value)
            val = -1 * heappop(value)
            ans = []
            for k, v in freq.items():
                if v == val:
                    ans.append(k)
            ans.sort()
            while ans[0] in answer:
                ans.pop(0)
            answer.append(ans[0])
            

        return answer
