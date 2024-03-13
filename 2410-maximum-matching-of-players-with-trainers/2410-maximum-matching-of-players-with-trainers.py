class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        ptr1 = 0
        ptr2 = 0
        players.sort()
        trainers.sort()
        count = 0
        while ptr1 < len(players) and ptr2 < len(trainers):
            if players[ptr1] <= trainers[ptr2]:
                count += 1
                ptr1 += 1
                ptr2 += 1
            else:
                ptr2 += 1
        return count