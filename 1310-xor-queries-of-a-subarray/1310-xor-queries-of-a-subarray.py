class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor = [0]
        xor_value = 0

        for num in arr:
            xor_value ^= num
            xor.append(xor_value)
        
        result = []
        for l, r in queries:
            result.append(xor[r + 1] ^ xor[l])
        
        return result