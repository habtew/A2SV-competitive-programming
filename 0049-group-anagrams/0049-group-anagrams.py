class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]


        maps = {}
        for word in strs:
            srtd = ''.join(sorted(word))
            if srtd in maps:
                maps[srtd].append(word)
            else:
                maps[srtd] = [word]
        return [val for val in maps.values()]