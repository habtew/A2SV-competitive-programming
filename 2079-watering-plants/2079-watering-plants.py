class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        count = 0
        i = 0
        cap_new = capacity

        while i < len(plants):
            if cap_new >= plants[i]:
                cap_new -= plants[i]
                count += 1
                i += 1
            else:
                count += 2 * i
                cap_new = capacity

        return count