class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = {}

        for word in re.split("\W+", paragraph):
            word = word.lower()
            if word not in banned and word in words and word != '':
                words[word] += 1
            elif word not in banned and word not in words and word != '':
                words[word] = 1

        return sorted(words.items(), key = lambda x: -x[1])[0][0]