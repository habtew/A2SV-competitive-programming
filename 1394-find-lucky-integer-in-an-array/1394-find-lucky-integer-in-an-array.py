class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counted = Counter(arr)
        
        larg = -1
        for key, val in counted.items():
            if key == val:
                if key > larg:
                    larg = key
        return larg