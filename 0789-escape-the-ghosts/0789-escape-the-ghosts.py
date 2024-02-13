class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        my_distance = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            gost_distance = abs(target[0] - ghost[0]) + abs(target[1] - ghost[1])
            if gost_distance <= my_distance:
                return False
        return True