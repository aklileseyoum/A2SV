class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = {}
        for index in range(len(s)):
            counter[s[index]] = index

        maximum = counter[s[0]]
        prev = 0
        answer = []

        for index in range(len(s)):
            if counter[s[index]] >= maximum:
                maximum = counter[s[index]]
                if index == maximum:
                    answer.append(maximum - prev + 1)
                    prev = maximum + 1
                    maximum += 1

        return answer
