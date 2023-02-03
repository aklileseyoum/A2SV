class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        player = len(players) - 1
        trainer = len(trainers) - 1
        count = 0

        while player >= 0 and trainer >= 0:
            if players[player] > trainers[trainer]:
                player -= 1
            else:
                count += 1
                player -= 1
                trainer -= 1

        return count
