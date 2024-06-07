class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sent = sentence.split(' ')
        for i in range(len(sent)):
            for word in dictionary:
                if sent[i].startswith(word):
                    sent[i] = word
        return ' '.join(sent)