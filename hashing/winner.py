"""
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.
"""
from collections import defaultdict
class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]] :
        players = set()
        losses_hashmap = defaultdict(int)

        for winner, loser in matches :
            players.add(winner)
            players.add(loser)
            losses_hashmap[loser] += 1

        lost_none = []
        lost_one = []

        for player in players :
            if player not in losses_hashmap :
                lost_none.append(player)
            elif losses_hashmap[player] == 1:
                lost_one.append(player)
        answer = [sorted(lost_none), sorted(lost_one)]
        return answer

if __name__ == "__main__":
    sol = Solution()
    assert sol.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]) == [[1,2,10],[4,5,7,8]], "Test Case 1 Failed"
    print("All test cases passed!")