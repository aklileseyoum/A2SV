class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        
        for index in range(len(boxes)):
            ans = 0

            if index != 0:
                for index2 in range(index):
                    if boxes[index2] == "1":
                        ans += index - index2

            if index != len(boxes) - 1:
                for index3 in range(index+1, len(boxes)):
                    if boxes[index3] == "1":
                        ans += index3 - index

            answer.append(ans)

        return answer
