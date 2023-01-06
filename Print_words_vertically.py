class Solution:
    def printVertically(self, s: str) -> List[str]:
        answer = []
        string = list(s.split(" "))
        length = []
        for i in string:
            length.append(len(i))
        maximum = max(length)
        
        for i in range(maximum):
            ans = ""
            for j in range(len(string)):
                if i >= len(string[j]):
                    ans += " "
                else:
                    ans += string[j][i]

            while ans[-1] == " ":
                ans = ans[:-1]
            answer.append(ans)

        return answer
