class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from collections import defaultdict
        answer = defaultdict(list)
        for num in nums:
            num = str(num)
            answer[num[0]].append(int(num))

        answers = sorted(answer.items(), reverse=True)
        number = ""
        for answer in answers:
            if len(answer[1]) > 1:
                for i in range(len(answer[1])-1):
                    j = 0
                    while j < len(answer[1])-1:
                        compare1 = str(answer[1][j]) + str(answer[1][j+1])
                        compare2 = str(answer[1][j+1]) + str(answer[1][j])
                        if int(compare2) > int(compare1):
                            answer[1][j], answer[1][j+1] = answer[1][j+1], answer[1][j]
                        j += 1
                for num in answer[1]:
                    number += str(num)
            else:
                num = answer[1][0]
                number += str(num)
        
        if int(number) == 0:
            number = "0"

        return number
