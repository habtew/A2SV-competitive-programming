class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        larg = max(candies)
        result = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= larg:
                result.append(True)
            else:
                result.append(False)
        return result
