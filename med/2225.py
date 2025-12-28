from collections import defaultdict


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = defaultdict(int)
        losers = defaultdict(int)
        
        lost_once = []
        for match in matches:
            winners[match[0]] += 1
            losers[match[1]] += 1
            
        havent_lost = list(set(winners.keys()) - set(losers.keys()))
        
        for loser in losers.keys():
            if losers[loser] == 1:
                lost_once.append(loser)
                
        return [sorted(havent_lost), sorted(lost_once)]