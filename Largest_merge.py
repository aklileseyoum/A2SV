class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        answer = ""
        pt1 = 0
        pt2 = 0
        
        while pt1 < len(word1) and pt2 < len(word2):
            if word1[pt1:] > word2[pt2:]:
                answer += word1[pt1]
                pt1 += 1
            else:
                answer += word2[pt2]
                pt2 += 1

        if pt1 < len(word1):
            answer += word1[pt1:]
        if pt2 < len(word2):
            answer += word2[pt2:]

        return answer
