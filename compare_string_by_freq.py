class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        q_no = []
        for query in queries:
            query = list(query)
            query.sort()
            query = Counter(query)
            q_no.append(list(query.values())[0])

        word_no = []
        for word in words:
            word = list(word)
            word.sort()
            word = Counter(word)
            word_no.append(list(word.values())[0])
        
        answer = []
        word_no.sort()
        length = len(word_no)
        for no in q_no:
            left = 0
            right = len(word_no) - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if word_no[mid] > no:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1

            if ans == -1:
                answer.append(0)
            else:
                answer.append(length - ans)
            

        return answer