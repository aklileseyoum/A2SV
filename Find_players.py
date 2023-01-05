class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loses = {}
        for match in matches:
            if match[0] not in loses:
                loses[match[0]] = 0
            
            if match[1] in loses:
                loses[match[1]] += 1
            else:
                loses[match[1]] = 1

        no_lost = []
        one_lost = []
        for key in loses:
            if loses[key] == 0:
                no_lost.append(key)
            elif loses[key] == 1:
                one_lost.append(key)

        no_lost.sort()
        one_lost.sort()

        answer = []
        answer.append(no_lost)
        answer.append(one_lost)

        return answer
