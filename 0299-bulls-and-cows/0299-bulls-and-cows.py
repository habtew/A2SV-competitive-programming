class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        no_cows, no_bulls = 0, 0
        secret_count, guess_count = Counter(secret), Counter(guess)

        for s, g in zip(secret, guess):
            if s == g:
                no_bulls += 1
                secret_count[s] -= 1
                guess_count[g] -= 1
        
        for s, g in zip(secret, guess):
            if s != g and secret_count[g] > 0:
                no_cows += 1
                secret_count[g] -= 1
        return f"{no_bulls}A{no_cows}B"