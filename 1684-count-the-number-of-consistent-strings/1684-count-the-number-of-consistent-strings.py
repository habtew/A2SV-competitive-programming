class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        def isConsistent(f, s):
            for c in s:
                if c not in f:
                    return False       
            return True

        count = 0
        for word in words:
            if isConsistent(allowed, word):
                print(word)
                count += 1
        return count