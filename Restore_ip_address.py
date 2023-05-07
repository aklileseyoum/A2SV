class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        answer = []

        if len(s) > 12:
            return answer

        def backtracking(idx, dot, ip):
            if dot == 4 and idx == len(s):
                answer.append(ip[:-1])
                return
            
            if dot > 4:
                return

            for idx2 in range(idx, min((idx+3), len(s))):
                if int(s[idx:idx2+1]) < 256 and (idx==idx2 or s[idx] != "0"):
                    backtracking(idx2+1, dot+1, ip+s[idx:idx2+1]+".")

        backtracking(0, 0, "")
        return answer
        