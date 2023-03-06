class Solution:
    def myPow(self, num: float, power: int) -> float:
        if power == 0:
            return 1

        if power < 0:
            return  self.myPow(1 / num, abs(power))
        
        answer = self.myPow(num, power // 2)

        if power % 2 == 1:
            return num * answer * answer
        else:
            return answer * answer