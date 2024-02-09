class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, losers = {}, {}
        for winner, loser in matches:
            if winner in winners:
                winners[winner] += 1
            else:
                winners[winner] = 1
            if loser in losers:
                losers[loser] += 1
            else:
                losers[loser] = 1
        not_lost = [item for item in winners if item not in losers]
        lost_one = [item for item in losers if losers[item] == 1]
        return [sorted(not_lost), sorted(lost_one)]