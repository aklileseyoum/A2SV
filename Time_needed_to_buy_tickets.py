class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        answer = 0
        num = tickets[k]
        for idx in range(len(tickets)):
            if idx > k:
                if num <= tickets[idx]:
                    answer += num - 1
                else:
                    answer += tickets[idx]
            else:
                if num < tickets[idx]:
                    answer += num
                else:
                    answer += tickets[idx]

        return answer
