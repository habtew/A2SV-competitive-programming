class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        invalid_nums = set()

        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                invalid_nums.add(fronts[i])

        smallest = float('inf')
        for i in range(len(fronts)):
            if fronts[i] not in invalid_nums:
                smallest = min(smallest, fronts[i])
            if backs[i] not in invalid_nums:
                smallest = min(smallest, backs[i])

        return smallest if smallest != float('inf') else 0
