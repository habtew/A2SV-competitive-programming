class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        dPointer = len(s)
        ipointer = 0
        result = []
        for i in range(len(s)):
            if s[i] == 'I':
                result.append(ipointer)
                ipointer += 1
            else:
                result.append(dPointer)
                dPointer -= 1
        result.append(ipointer)
        return result