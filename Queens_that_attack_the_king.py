class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        directions = [[1,0], [0,1], [0,-1], [-1,0], [1,1], [-1,-1], [-1,1], [1,-1]]
        direction = [[]*2]*8
        answer = []
        for i in range(1,9):
            direction = [[j*i for j in item]for item in directions]
            for j in direction:
                if len(j) == 2:
                    new = [king[0]+j[0], king[1]+j[1]]
                    if new in queens:
                        answer.append(new)
                        to_be_removed= [j[0]/i, j[1]/i]
                        directions.remove(to_be_removed)

        return answer
