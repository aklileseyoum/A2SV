class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        last = len(skill) - 1
        first = 0
        summ = skill[first] + skill[last]
        answer = 0
        while first < last:
            sum2 = skill[first] + skill[last]
            if summ != sum2:
                return -1
            else:
                answer += skill[first] * skill[last]
            first += 1
            last -= 1


        return answer
