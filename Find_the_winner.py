class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        count = 0
        players = []
        for i in range(1, n+1):
            players.append(i)

        idx = 0
        while len(players) > 1:
            if idx == len(players):
                idx = 0
            count += 1
            if count == k:
                players.pop(idx)
                count = 0
            else:
                idx += 1

        return players[0]
